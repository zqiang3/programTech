## 介绍

inspect模块用于收集python对象的信息，可以获取类或函数的参数的信息，源码，解析堆栈，对对象进行类型检查等等，有几个好用的方法

***getmembers(object[, predicate])***

返回一个包含对象的所有成员的(name, value)列表。返回的内容比对象的__dict__包含的内容多，源码是通过dir()实现的。

