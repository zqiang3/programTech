## 数组初始化

1. 

```java
// arrayName = new type[]{element1,element2,element3...}
int[] arr;
arr = new int[]{1, 2, 3};
```



## 接口

```java
class Employee implements Comparable 
```

## 类

* 用Java编写的所有代码都位于某个类的内部。没有类就不能做任何事情。

* 通过扩展一个类来构建其他类称为**继承**。

* 对象中的数值称为实例域，操纵数据的过程称为方法。

* 每个类实例（对象）都有一组实例域值，这些值的集合就是这个对象当前的**状态**。

* 对象的状态必须通过调用方法来实现。否则，只能说明对象的封装性遭到了破坏。
* 在一个源文件中，只能有一个仅有类。
* 在Java中，所有的方法都必须在类的内部定义，但并不表示它们是内联方法。是否成为内联方法由虚拟机决定。

### 类之间的关系

* 依赖：use-a，一个类操纵另一个类的对象
* 聚合：has-a
* 继承：is-a



### 构造器

构造器的名字与类名相同。

构造器没有返回值。

构造器总是伴随new操作符一起调用。

所有的Java对象都是在堆中构造的。

如果编写构造器，系统会默认提供一个无参数构造器。若有至少一个构造器，系统就不提供无参数构造器。

### 对象的引用

一个对象变量仅仅引用一个对象。

局部变量并不自动初始为null

### 自定义类

```
class Employee
{
	field1,
	filed2,
	...
	constructor1,
	constructor2,
	...
	method1,
	method2
}
```



### 获得或设置实例域

* 一个私有的实例域
* 一个公有的域访问器方法
* 一个公有的域更改器方法

###  静态域与静态方法

静态域属于类，不属于任何独立的对象。

静态变量使用得比较少，静态常量却使用得比较多。

静态方法不能操作对象。

可以使用对象名调用静态方法，但是不建议。



### 重载

相同的名字，不同的参数，是重载。

要完整地描述一个方法，需同时用方法名和参数。

返回类型不是方法签名的一部分。



### 默认域初始化

如果没有在构造器为域明确初始化值，就会自动为域设置默认零值。这是域与局部变量主要的不同点。

### 显示域初始化

在类定义中，直接将一个值赋给域。在执行构造器前，先执行赋值操作。



### 使用细节

所有方法中最好不要用跟实例域同名的变量。

不要返回可变对象的引用。

方法可以访问所属类的私有属性，而不限于访问隐式参数的私有属性。

每一个类可以有一个main方法，这是一个对类进行单元测试的技巧。