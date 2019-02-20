## 示例

```python
#coding: utf-8
import time
import os
from multiprocessing import Process

def task(name):
    print 'child id: ', os.getpid()     
    print name
    

print 'parent id: ', os.getpid()
p = Process(target=task, args=('子进程1',))
p.start()
time.sleep(3)
print '主进程'
```

