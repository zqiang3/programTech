字典类型在获取键的值时始终会尝试调用`__missing__`。`defaultdict`做的工作也只是提供了一种`__missing__`的实现。如果你自己提供了`__missing__`，你也不必实现`defaultdict`的子类。