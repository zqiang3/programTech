## wsgi是什么

wsgi is the web server gateway interface.

1. 浏览器发送一个HTTP请求
2. 服务器收到请求，生成响应内容
3. 服务器把响应内容返回给浏览器
4. 浏览器收到响应，展示内容

最简单的Web应用就是先把HTML用文件保存好，用一个现成的HTTP服务器软件，接收用户请求，从文件中读取HTML，返回。Apache、Nginx、Lighttpd等这些常见的静态服务器就是干这件事情的。

我们用python专注于生成HTML文档，不希望接触到TCP连接、HTTP原始请求和响应格式。WSGI是一个统一的接口，让我们专心用python写Web业务。

WSGI接口定义非常简单，它只要求Web开发者实现一个函数，就可以响应HTTP请求。

```python
def application(environ, start_response):
	start_response('200 OK', [('Content-Type', 'text/html')])
	return '<h1>Hello, web!</h1>'
```

上面的`application()`函数就是符合WSGI标准的一个HTTP处理函数，它接收两个参数：

- environ：一个包含所有HTTP请求信息的`dict`对象；
- start_response：一个发送HTTP响应的函数。

有了WSGI，我们关心的就是如何从`environ`这个`dict`对象拿到HTTP请求信息，然后构造HTML，通过`start_response()`发送Header，最后返回Body。

不过，等等，这个`application()`函数怎么调用？如果我们自己调用，两个参数`environ`和`start_response`我们没法提供，返回的`str`也没法发给浏览器。

所以`application()`函数必须由WSGI服务器来调用。



无论多么复杂的Web应用程序，入口都是一个WSGI处理函数。HTTP请求的所有输入信息都可以通过`environ`获得，HTTP响应的输出都可以通过`start_response()`加上函数返回值作为Body。

## python自带的wsgi web server

```python
# server.py
from wsgiref.simple_server import make_server
from hello import application

httpd = make_server('', 8000, application)
print 'Saving HTTP on port 8000'

httpd.serve_forever()
```

```python
# hello.py
def application(environ, start_response):
    method = environ['REQUEST_METHOD']
    path = environ['PATH_INFO']
    if method == 'GET' and path == '/':
        return handle_home(environ, start_response)
    if method == 'POST' and path == 'sign':
        return handle_sign(environ, start_response)
```

## Flask示例

```pyton
# app.py
from flask import Flask
from flask import request 

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def home():
    return '<h1>Home</h1>'


@app.route('/signin', methods=['GET'])
def signin_form():
    return '''
    <form action='/sign' method='post'>
    <p><input name="username"></p>
    <p><input name="password" type="password"></p>
    <p><button type="submit">sign in</button></p>
    </form>
'''

@app.route('/sign', methods=['POST'])
def signin():
    if request.form['username'] == 'admin' and request.form['password'] == 'password':
        return '<h3>hello, admin</h3>'

    return '<h3>Bad user name or password</h3>'


if __name__ == '__main__':
    app.run('0.0.0.0', 8000)
```

## 参考链接

https://www.jianshu.com/p/679dee0a4193

https://blog.csdn.net/a519640026/article/details/76157976

## 几个概念

**WSGI协议**：全称是`Web Server Gateway Interface`，即web服务器网关接口。`WSGI`不是服务器，`python`模块，框架，`API`或者任何软件，只是一种规范，描述`web server`如何与`web application`通信的规范。

**uwsgi：**与`WSGI`一样是一种通信协议，是`uWSGI`服务器的独占协议，用于定义传输信息的类型(`type of information`)，每一个`uwsgi packet`前`4byte`为传输信息类型的描述，与WSGI协议是两种东西，据说该协议是`fcgi`协议的10倍快。

**uWSGI：**是一个`web`服务器，实现了`WSGI`协议、`uwsgi`协议、`http`协议等。

## WSGI协议规范

`WSGI`协议主要包括`server`和`application`两部分：

- `WSGI server`负责从客户端接收请求，将`request`转发给`application`，将`application`返回的`response`返回给客户端；
- `WSGI application`接收由`server`转发的`request`，处理请求，并将处理结果返回给`server`。`application`中可以包括多个栈式的中间件(`middlewares`)，这些中间件需要同时实现server与application，因此可以在WSGI服务器与WSGI应用之间起调节作用：对服务器来说，中间件扮演应用程序，对应用程序来说，中间件扮演服务器。

`WSGI`协议其实是定义了一种`server`与`application`解耦的规范，即可以有多个实现`WSGI server`的服务器，也可以有多个实现`WSGI application`的框架，那么就可以选择任意的`server`和`application`组合实现自己的`web`应用。例如`uWSGI`和`Gunicorn`都是实现了`WSGI server`协议的服务器，`Django`，`Flask`是实现了`WSGI application`协议的`web`框架，可以根据项目实际情况搭配使用。

像`Django`，`Flask`框架都有自己实现的简单的`WSGI server`，一般用于服务器调试，生产环境下建议用其他`WSGI server`。

Web server运行Web application

## 请求传递详解

![WSGI](http://imgbox.com/mrbsG2Ts)

## 示例

```python
def application(environ, start_response):
    status = '200 OK'
    output = 'Hello, world'
    response_headers = [
        ('Content-type', 'text/plain'),
        ('Content-length', str(len(output)))
    ]
    start_response(status, response_headers)
    return [output]
```

```sh
uwsgi --http 0.0.0.0:8000 --wsgi-file userver.py --master --processes 4 --threads 2
```

执行这个命令会产生4个uwsgi进程（每个进程2个线程），1个master进程，当有子进程死掉时再产生子进程，1个 the HTTP router进程，一个6个进程。

这个Http route进程的地位有点类似nginx，(可以认为与nginx同一层)负责路由http请求给worker, Http route进程和worker之间使用的是uwsgi协议