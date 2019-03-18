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
```

