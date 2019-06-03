## 可调用对象

我们平时自定义的函数、内置函数和类都属于可调用对象，但凡是可以把一对括号()应用到某个对象身上都可称之为可调用对象，判断对象是否为可调用对象可以用函数 callable。

如果在类中实现了 `__call__` 方法，那么实例对象也将成为一个可调用对象。



## 应用场景

类可以记录数据，而函数不行（闭包某种意义上可行），利用这种特性可以实现基于类的装饰器，在类里记录状态。

```python
class Counter:
    def __init__(self, func):
        self.func = func
        self.count = 0

    def __call__(self, *args, **kwargs):
        self.count += 1
        return self.func(*args, **kwargs)

@Counter
def foo():
    pass

for i in range(10):
    foo()

print(foo.count)  # 10
```

