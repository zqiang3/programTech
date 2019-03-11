MediaType，即是Internet Media Type，互联网媒体类型；也叫做MIME类型，在Http协议消息头中，使用Content-Type来表示具体请求中的媒体类型信息。

```bash
  类型格式：type/subtype(;parameter)? type
  主类型，任意的字符串，如text，如果是*号代表所有； 
  subtype 子类型，任意的字符串，如html，如果是*号代表所有； 
  parameter 可选，一些参数，如Accept请求头的q参数， Content-Type的 charset参数。 
```

常见的媒体格式类型如下：

    text/html ： HTML格式
    text/plain ：纯文本格式      
    text/xml ：  XML格式
    image/gif ：gif图片格式    
    image/jpeg ：jpg图片格式 
    image/png：png图片格式
---------------------
