```c
unsigned sleep(unsigned seconds);
```



## 中断时sleep会失效

sleep（）运行时程序捕获到一个信号，那么这个信号就会中断sleep，去执行信号所指内容，等处理好信号之后，程序会直接跳到sleep的下一行执行，那么即使sleep秒数没有数完，也照样结束。这就是造成sleep失效的原因。