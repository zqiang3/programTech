```python
class Cat(object):
    a = 2
    b = 3
    def __init__(self, name, age):
        self.name = name
        self.age = age


cat = Cat('pipi', 1)
print cat.__dict__
print Cat.__dict__
```

'int' object has no attribute`__dict__`

总结：

1. 内置的数据类型没有__dict__属性 
2. 每个类有自己的__dict__属性，就算存着继承关系，父类的__dict__ 并不会影响子类的__dict__ 
3. 对象也有自己的__dict__属性， 存储self.xxx 信息，父子类对象公用__dict__ 