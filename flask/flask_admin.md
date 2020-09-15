## 快速开始

```python
from flask import Flask
from flask_admin import Admin

app = Flask(__name__)

admin = Admin(app, name='microblog', template_mode='bootstrap3')
# Add administrative views here

app.run()
```





## 增加视图

```python
class MyView(BaseView):
    @expose('/')
    def index(self):
        return self.render('index.html')


admin.add_view(MyView(name=u'Hello'))
```

