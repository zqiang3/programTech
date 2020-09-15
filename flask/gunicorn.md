## 简介

Gunicorn“绿色独角兽”是一个被广泛使用的高性能的Python WSGI UNIX HTTP服务器，移植自Ruby的独角兽（Unicorn ）项目,使用pre-fork worker模式，具有使用非常简单，轻量级的资源消耗，以及高性能等特点。
Gunicorn 服务器作为wsgi app的容器，能够与各种Web框架兼容（flask，django等）,得益于gevent等技术，使用Gunicorn能够在基本不改变wsgi app代码的前提下，大幅度提高wsgi app的性能。



## 架构模型

Gunicorn是基于 pre-fork 模型的。也就意味着有一个中心管理进程( master process )用来管理 worker 进程集合。Master从不知道任何关于客户端的信息。所有的请求和响应处理都是由 worker 进程来处理的。



总结：gunicorn 会启动一组 worker进程，所有worker进程公用一组listener，在每个worker中为每个listener建立一个wsgi server。每当有HTTP链接到来时，wsgi server创建一个协程来处理该链接，协程处理该链接的时候，先初始化WSGI环境，然后调用用户提供的app对象去处理HTTP请求。

## 安装

```bash
pip install gunicorn
easy_install gunicorn
```

或下载源码安装

```bash
1 git clone git://github.com/benoitc/gunicorn.git
2 cd gunicorn
3 sudo python setup.py install　
```



支持异步worker需要下载以下三个包

```bash
1 easy_install -U greenlet
2 easy_install -U eventlet
3 easy_install -U gevent 
```



若安装gevent失败，可能需要安装python headers

```bash
sudo apt-get install python-dev
```

gunicorn还需要库函数 libevent(1.4.x or 2.0.4)



APP_MODULE 指定 wsgi application文件,书写格式 $(MODULE_NAME):$(VARIABLE_NAME)。其中 module_name用来制定将要运行的 wsgi application文件,可是一个完整的点缀名。比如当前目录 myapp 目录下有个 Python 包 gunicorn_app, gunicorn_app包下有一个wsgi application文件 test.py 则 module_name可以直接写成  gunicorn_app.test。viriable_name表示在 module_name 文件中要调用的对象(是一个WSGI callable, 可以是一个函数,类详情参看[WSGI规格说明书](http://www.cnblogs.com/ArtsCrafts/p/wsgi.html))名



## 基本用法 

quick rundown

```bash
$ pip install gunicorn
  $ cat myapp.py
    def app(environ, start_response):
        data = b"Hello, World!\n"
        start_response("200 OK", [
            ("Content-Type", "text/plain"),
            ("Content-Length", str(len(data)))
        ])
        return iter([data])
  $ gunicorn -w 4 myapp:app
  [2014-09-10 10:22:28 +0000] [30869] [INFO] Listening at: http://127.0.0.1:8000 (30869)
  [2014-09-10 10:22:28 +0000] [30869] [INFO] Using worker: sync
  [2014-09-10 10:22:28 +0000] [30874] [INFO] Booting worker with pid: 30874
  [2014-09-10 10:22:28 +0000] [30875] [INFO] Booting worker with pid: 30875
  [2014-09-10 10:22:28 +0000] [30876] [INFO] Booting worker with pid: 30876
  [2014-09-10 10:22:28 +0000] [30877] [INFO] Booting worker with pid: 30877
```





```bash
gunicorn myapp.test:app
gunicorn --workers=4 --bind=127.0.0.1:8000 myapp.test:app
```

编写配置文件

```python
# config.py
import multiprocessing

bind = "127.0.0.1:8001"
workers = multiprocessing.cpu_count() * 2 + 1
```



使用配置文件启动gunicorn

```bash
gunicorn --config=config.py --worker-class=eventlet myapp.test:app
```

worker-class默认是sync(同步),我们配置成了 eventlet(并发的)