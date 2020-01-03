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

