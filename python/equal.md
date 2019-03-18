在java中，对于两个对象啊a，b，若a==b表示，a和b不仅值相等，而且指向同一内存位置，若仅仅比较值相等，应该用equals。而在python中对应上述两者的是is 和==。

python中，`a is b`不仅表示值相等，而且两个引用指向内存同一位置。而`a == b`仅表示a和b的值相等

```python
class Num(object):
    def __init__(self, val):
        self.val = val


    def __eq__(self, other):
        print 'Num.__equal__'
        return self.val == other.val
    
    

n1 = Num(3)
n2 = Num(3)
print n1 == n2
print n1 is n2
```

