下面格式的意思是从同级导包，但什么情况才能这样写呢？

```python
"""my_name.py"""
from . import xxx
from .xxx import xxx
```



`print(__name__)`


充要条件：本模块内__name__的值是 'package_xx.my_name' 格式 且 想要从同级开始导入东西时。

补充：package_xx可以是多层，但最少1层。

推测：那个点的意思就是把__name__的值退一层

 

推广： __name__的值中有n个点  ==> from 后能以m(m<=n)个点开头

补充：按需选择m的值，一个点表示从__name__退一层
