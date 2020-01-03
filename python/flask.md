## 一个最小的应用

```python
from flask import Flask
app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'Hello World!'

if __name__ == '__main__':
    app.run()			
```

## 调试模式

```python
app.debug = True
app.run()
# 或
app.run(debug=True)
```





## 路由

 [`route()`](http://docs.jinkan.org/docs/flask/api.html#flask.Flask.route) 装饰器把一个函数绑定到对应的 URL 上。

```python
@app.route('/')
def index():
	return 'Index Page'

@app.route('/hello')
def hello():
  return 'Hello world'
```

`<converter:variable>`

| int   | 接受整数   |
| ----- | ---------- |
| float | 接受浮点数 |
| path  | 也接受斜线 |



动态路由**

可以把特殊的字段标记为`<variable_name>`，这个部分将会作为命名参数传递到你的函数。

```python
@app.route('/user/<username>')
def show_user_profile(username):
  return 'User %s' % username
  
@app.route('/post/<int:post_id>')
def show_post(post_id):
  return 'Post %d' % post_id

@app.route('/path/<path:subpath>')
def show_subpath(subpath):
    # show the subpath after /path/
    return 'Subpath %s' % escape(subpath)
```



## 唯一URL/重定向行为

```python
@app.route('/projects/')
def projects():
  return 'The project page'
```



## blueprint

views/index.py

```python
from flask import Blueprint, render_template

index_blueprint = Blueprint('index', __name__)

@index_blueprint.route("/")
def index():
    return "Hello World!"
```

app.py

```python
from flask import Flask
from views.index import index_blueprint

application = Flask(__name__)
application.register_blueprint(index_blueprint)
```



run application

```bash
$ export FLASK_APP=app.py
$ flask run
```



## Accessing Request Data



request为什么可以是全局的，如何做到线程安全？

context locals



## Flask线程间上下文安全

启动之后在进程里维护request栈和app栈，通过线程ID来保证每个请求的线程安全

主要依赖三个类`Local`, `LocalStack`和`LocalProxy`



**1. Local**

先看Local的源码，实质并不是Flask中定义的，而是Flask依赖的werkzeug库所定义。

可以看到其定义的两个属性`__storage__`， `__ident_func__`以及三个方法`__getattr__`, `__setattr__`, `__release_local__`。

