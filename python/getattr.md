## getattr

```python
class Student(object):
  name = 'aaa'
  
  def run(self):
    pass
  
s = Student()
print(getattr(s, 'name'))
getattr(s, 'run')()     # 获取run方法，后面加括号可以将这个方法运行

getattr(t, "age")       # 获取一个不存在的属性，报AttributeError
getattr(t, "age","18")  # 若属性不存在，返回一个默认值。
```



## 使用getattr轻松实现工厂模式

```python
import statout
def output(data, format='text'):
  func = getattr(statout, 'output_%s' % format)
  return func(data)
```



## `__getattr__`

`object. __getattr__(self, name)`是一个对象方法，如果找不到对象的属性时会调用这个方法。

这个方法应该返回属性值或者抛出`AttributeError`异常。

注意，如果通过正常机制能找到对象属性的话，不会调用`__getattr__`方法。

```python
>>> class Frob:
...     def __init__(self, bamf):
...         self.bamf = bamf
...     def __getattr__(self, name):
...         return 'Frob does not have `{}` attribute.'.format(str(name))
...
>>> f = Frob("bamf")
>>> f.bar
'Frob does not have `bar` attribute.'
>>> f.bamf
'bamf'
```

