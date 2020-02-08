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



```python
from flask import request

request.form['name']  # for POST, PUT
request.args['name']  # for GET
```





## Flask线程间上下文安全

启动之后在进程里维护request栈和app栈，通过线程ID来保证每个请求的线程安全

主要依赖三个类`Local`, `LocalStack`和`LocalProxy`



**1. Local**

先看Local的源码，实质并不是Flask中定义的，而是Flask依赖的werkzeug库所定义。

可以看到其定义的两个属性`__storage__`， `__ident_func__`以及三个方法`__getattr__`, `__setattr__`, `__release_local__`。



主线程中生成一个对象local=Local()，三个线程中进行相同的操作local.no=每个线程对应的数。为每个线程都开辟一个存储，所以谁来取或者存就找到自己对应中的位置，虽然取得key都一样，但是每次存取都是只关于自己的值。



## redirect

```python
from flask import abort, redirect, url_for

@app.route('/')
def index():
    return redirect(url_for('login'))

@app.route('/login')
def login():
    abort(401)
    this_is_never_executed()
```

## response

1. If a response object of the correct type is returned it’s directly returned from the view.
2. If it’s a string, a response object is created with that data and the default parameters.
3. If it’s a dict, a response object is created using `jsonify`.
4. If a tuple is returned the items in the tuple can provide extra information. Such tuples have to be in the form `(response, status)`, `(response, headers)`, or `(response, status, headers)`. The `status` value will override the status code and `headers` can be a list or dictionary of additional header values.
5. If none of that works, Flask will assume the return value is a valid WSGI application and convert that into a response object.



或者你可以直接构造一个`response`对象

`make_response` 给开发者提供了添加`header`的手段

```python
@app.errorhandler(404)
def not_found(error):
    resp = make_response(render_template('error.html'), 404)
    resp.headers['X-Something'] = 'A value'
    return resp
```

##APIs with JSON

A common response format when writing an API is JSON. It’s easy to get started writing such an API with Flask. If you return a `dict` from a view, it will be converted to a JSON response.

```python
@app.route("/me")
def me_api():
    user = get_current_user()
    return {
        "username": user.username,
        "theme": user.theme,
        "image": url_for("user_image", filename=user.image),
    }
```

or use `jsonify()` to serialize any supported JSON data type.



## extensions

### flask-babelex

installation

```bash
easy_install Flask-BabelEx
pip install Flask-BabelEx
```

configuration

```python
from flask import Flask
from flask.ext.babelex import Babel

app = Flask(__name__)
app.config.from_pyfile('mysettings.cfg')
babel = Babel(app)
```

### 题外话，Flask 0.8引入重定向导入系统

ext是python特有的拓展功能，目前，扩展必须支持Python 2.6以及Python 2.7

原因：

> 扩展导入转换
>
> 我们推荐使用Flask扩展的命名空间包。这在实践中证明是有问题的，因为存在许多不同的竞争命名空间包系统，并且pip会在不同系统之间自动切换，并且这给用户造成了很多问题。
> 相反，我们现在推荐命名软件包flask_foo，而不是现在已弃用的flaskext.foo。 Flask 0.8引入了一个重定向导入系统，该系统可以使用来自flask.ext.foo的导入，并且它将首先尝试flask_foo，并且如果失败，则flaskext.foo。
> Flask扩展应该促使用户从flask.ext.foo而不是flask_foo或flaskext_foo导入，以便扩展可以转换到新的软件包名称而不会影响用户。





## configuration

flask的config是`dict`的一个子类。