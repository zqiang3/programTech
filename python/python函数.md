python函数的**参数可以有名称和位置**，可以给只定义了位置参数的函数传递命名参数，反之，也可以通过位置的方式传递给定义了命名参数的函数。

```python
def foo(x, y=0):
    return x - y

foo(3, 1)      # 2
foo(3)         # 3
foo()
#Traceback:
    #TypeError: foo() takes at least 1 argument (0 given)
foo(y=1, x=3)  # 5
```



### 内嵌函数

内部函数处于外部函数的作用域内

简单例子：

```python
def foo():
	def bar():
		print 'this is bar()'
	print 'this is foo()'
	
foo()
bar()  # error
```

```python
def foo():
	n = 3
	def bar():
		n -= 1   # error
		print 'this is bar()'
	print 'this is foo()'
	
foo()
```



```python
def outer():
    x = dict(age=12)
    def inner():
        print 'outer x, ', id(x)
        print x
    print inner
    return inner


func = outer()
print func
func()

func2 = outer()
print func2
func2()
```

每次函数outer被调用时，函数inner都会被重新定义，如果不把它当做变量返回的话，每次执行过后它将不复存在。

## 函数是python世界里的一级类对象

```python
issubclass(int, object)            # True
def foo():
    pass
foo.__class__                      # <type 'function'>
issubclass(foo.__class__, object)  # True
```

## 闭包

```python
def outer():
     x = 1
     def inner():
         print x # 1
     return inner
foo = outer()
foo.func_closure # doctest: +ELLIPSIS
(<cell at 0x: int object at 0x>,)
```

所有的东西都在python的作用域规则下进行工作：“x是函数outer里的一个局部变量。当函数inner在#1处打印x的时候，python解释器会在inner内部查找相应的变量，当然会找不到，所以接着会到封闭作用域里面查找，并且会找到匹配。 

但是从变量的生存周期来看，该怎么理解呢？我们的变量x是函数outer的一个本地变量，这意味着只有当函数outer正在运行的时候才会存在。根据我们已知的python运行模式，我们没法在函数outer返回之后继续调用函数inner，在函数inner被调用的时候，变量x早已不复存在，可能会发生一个运行时错误。 

万万没想到，返回的函数inner居然能够正常工作。Python支持一个叫做函数闭包的特性，用人话来讲就是，嵌套定义在非全局作用域里面的函数能够记住它在被定义的时候它所处的封闭命名空间。这能够通过查看函数的func_closure属性得出结论，这个属性里面包含封闭作用域里面的值（只会包含被捕捉到的值，比如x，如果在outer里面还定义了其他的值，封闭作用域里面是不会有的) 

```python
def outer(x):
    def inner():
        print x
    return inner

print1 = outer(1)
print2 = outer(2)

print1()
print2()
```

闭包，被函数记住的封闭作用域

闭包单独拿出来就是一个非常强大的功能， 在某些方面，你也许会把它当做一个类似于面向对象的技术：outer像是给inner服务的构造器，x像一个私有变量。使用闭包的方式也有很多：你如果熟悉python内置排序方法的参数key，你说不定已经写过一个lambda方法在排序一个列表的列表的时候基于第二个元素而不是第一个。现在你说不定也可以写一个itemgetter方法，接收一个索引值来返回一个完美的函数，传递给排序函数的参数key。 

## 位置参数

```python
def one(*args):
     print args # 1
one()
()
one(1, 2, 3)
(1, 2, 3)
def two(x, y, *args): # 2
     print x, y, args
two('a', 'b', 'c')
a b ('c',)
```

Python允许我们制定一些参数并且通过args捕获其他所有剩余的未被捕捉的位置参数 

`*`操作符在函数被调用的时候也能使用。意义基本是一样的。当调用一个函数的时候， 一个用*标志的变量意思是变量里面的内容需要被提取出来然后当做位置参数被使用 

```python
def add(x, y):
     return x + y
lst = [1,2]
add(lst[0], lst[1]) # 1
3
add(*lst) # 2
3
```

*args要么是表示调用方法大的时候额外的参数可以从一个可迭代列表中取得，要么就是定义方法的时候标志这个方法能够接受任意的位置参数。 

## 关键字参数

接下来提到的**会稍多更复杂一点，**代表着键值对的餐宿字典，和*所代表的意义相差无几，也很简单对不对： 

```python
def foo(**kwargs):
     print kwargs
foo()
{}
foo(x=1, y=2)
{'y': 2, 'x': 1}

dct = {'x': 1, 'y': 2}
def bar(x, y):
     return x + y
bar(**dct)
3
```

当我们定义一个函数的时候，我们能够用**kwargs来表明，所有未被捕获的关键字参数都应该存储在kwargs的字典中。 