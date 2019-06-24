## uWSGI是如何工作的

<https://stone.moe/default/how-uwsgi-works.html>

人们常说，使用工具时，了解其中的原理才能用的更舒心，更加无所顾忌。
对于程序员来说更是如此。

抱着这样的心态，针对 Python 处理 HTTP 请求的工作过程做了实验，并做了一些总结归纳。

0x01 uwsgi 与 uWSGI 与 WSGI
\-
**WSGI**：编程接口协议，专为 Python 设计，用于 Web 开发 (类比 COM 编程接口协议)

```
WSGI 协议预先约定了一些 callee (Python) 必须实现的 callable (Function)，以使 caller 能正确调用 callee，来处理 HTTP 请求。
```

**uWSGI**：一个 WSGI 协议 caller 方的具体实现，使用 C 语言编写 (类比 COM 组件的调用方)

> ```
> uWSGI 是 caller 方，我们写的 Python 程序自然就是 callee 方了。
> uWSGI 可以通过 uwsgi 协议与 HTTP Server 进行通信，只作为调用 Python 处理请求的桥梁。
> uWSGI 当然也提供了一个 HTTP 服务器的功能，直接处理 HTTP 请求。
> ```

**uwsgi**：通信协议，描述了 HTTP Server 与 WSGI caller 如何通信（类比 CGI，FastCGI）

> ```
> 具体通信协议的差别在这里不再赘述，但值得一提的是：
> uwsgi 继承了 FastCGI 的并发优点，但不是通过多进程，而是通过消息分片的方式，在同一 Socket 上并发传输多个请求，这使得资源被更有效的利用了。
> ```

于是一个常规的处理过程是这样的：

> ```
> Client ==HTTP==> Nginx ==uwsgi==> uWSGI ==WSGI==> Python 程序
> ```

经过实验发现，uWSGI 通过将支持 WSGI 的 Python 程序载入到其每个 Worker Process 中，各作为单独的实例存在于内存中。在接受Web请求时，分配给各 Worker Process 进行处理。



## uWSGI的安装

uWSGI is a (big) C application, so you need a C compiler (like gcc or clang) and the Python development headers.

```bash
pip install uwsgi
# 或出错可能是缺少python-dev build-essential
sudo apt-get install python-dev
sudo apt-get install build-essential  # On a Debian-based distro
```



## uWSGI的主要特点
超快的性能
低内存占用，实测为apache2的mod_wsgi的一半左右
多app管理
详尽的日志功能，可以用来分析app性能和瓶颈
高度可定制，内存大小限制，服务一定次数后重启等

## quick start

uwsgi 

--http :9090 (或--socket --http-socket)

--wsgi-file foobar.py
--processes
--threads

--stats 127.0.0.1:9191

(The stats subsystem allows you to export uWSGI’s internal statistics as JSON)

--chdir  (move to a specific directory)

## WSGI application

```python
# foobar.py
def application(env, start_response):
    """test application
    """
    content = [
        ('Content-Type', 'text/html'),
    ]
    start_response('200 OK', content)
    res_str = 'Hello, {}\n'.format(__name__)
    return [res_str]
```



## 在前端放置nginx

Do not use `--http` when you have a frontend webserver or you are doing some form of benchmark, use `--http-socket`. Continue reading the quickstart to understand why.

### 使用uwsgi协议

nginx按如下方式配置：

```nginx
location / {
    uwsgi_pass 127.0.0.1:9090;
}
```

This means “pass every request to the server bound to port 9090 speaking the uwsgi protocol”.

nginx 会将每个请求转发到本地9090端口，使用的是uwsgi协议。

运行usgi：(注意使用 --socket)

```bash
uwsgi  --socket 127.0.0.1:9090 --wsgi-file testapp.py
```

## 使用http协议

nginx配置

```nginx
location / {
    proxy_pass http://127.0.0.1:9090;
}
```

运行usgi：(注意使用 --http-socket，不同于--http, --http是直接启一个http代理接收请求)

```bash
uwsgi  --http-socket 127.0.0.1:9090 --wsgi-file testapp.py
```

uwsgi_pass使用的是uwsgi协议，proxy_pass使用HTTP协议与uWSGI server交互。

## nginx和uwsgi的关系

nginx是前端服务器，负责接收请求。

uwsgi是一种通信协议，负责在服务器和应用程序间进行数据通信。

**通信过程**： 

客户端发送一个http请求，被nginx服务器接收，nginx服务器将请求转发给uWSGI,uWSGI将请求转发给实现uwsgi协议的应用程序(flask,gunicorn等等)

## uWSGI配置

chdir为项目路径
module为项目中的模块
enable-threads允许用内嵌的语言启动线程。这将允许你在app程序中产生一个子线程。
lazy-appsuwsgi 只要可能的情况下都用 fork() 来复制。默认，他会在加载应用后执行 fork 。如果你不想使用 --lazy选项。开启它，会知道uwsgi来加载应用。lazy模式优雅的重启works：代替重载的是，每个worker轮流着reload。如果你使用'lazy app loading'，但你想维持标准的uwsgi重载行为，在1.3之后你可以使用 --lazy-apps 选项。

touch-reload 优雅的重启uWSGI 