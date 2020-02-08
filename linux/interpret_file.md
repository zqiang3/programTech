假设解释器文件/dir/foo.sh内容为

```bash
#!/bin/sh param1
...
     
      <1>     <2>
```

而调用execl执行这个解释器文件的C代码为

```bash
 execl("/dir/foo.sh", "foo.sh", "myarg1", "MY ARG2", NULL);
  
                <A>           <B>      <C>       <D>
                             argv[0]  argv[1]   argv[2]
```

那么，新程序中的实际的参数分别为：

```bash
argv[0]: /bin/sh        <1>
argv[1]: param1         <2>
argv[2]: /dir/foo.sh    <A>
argv[3]: myarg1         <C>
argv[4]: MY ARG2        <D>
```

除了<1>和<2>，内核用execl的pathname（<A>）代替了原来的argv[0]（<B>），这是因为pathname一般含更有用的信息。