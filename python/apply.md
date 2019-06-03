apply()可以间接地调用函数

```python
def func(name, age):
	print 'hello'
    print name, age
    
args = ('zq', '30')
apply(hello, args)
```

