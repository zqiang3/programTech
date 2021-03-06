## 基本语法

类名：对于所有的类来说，类名首字母应该大写。

方法名：所有的方法名应该以小写字母开头。

源文件名：源文件名必须和类名相同。

一个源文件中只能有一个 public 类，可以有多个非public类。源文件的名称应该和 public 类的类名保持一致。

## Java修饰符

修饰符用来定义类、方法或者变量

访问控制修饰符：default, public, protected, private

非访问控制修饰符：final, abstract, static, synchronized



* **default** (即默认，什么也不写）: 在同一包内可见，不使用任何修饰符。使用对象：类、接口、变量、方法。
* **private** : 在同一类内可见。使用对象：变量、方法。 **注意：不能修饰类（外部类）**
* **public** : 对所有类可见。使用对象：类、接口、变量、方法
* **protected** : 对同一包内的类和所有子类可见。使用对象：变量、方法。 **注意：不能修饰类（外部类）**。

protected 可以修饰数据成员，构造方法，方法成员，**不能修饰类（内部类除外）**。

接口及接口的成员变量和成员方法不能声明为 protected。

*protected 是最难理解的一种 Java 类成员访问权限修饰词*



- 父类中声明为 public 的方法在子类中也必须为 public。
- 父类中声明为 protected 的方法在子类中要么声明为 protected，要么声明为 public，不能声明为 private。
- 父类中声明为 private 的方法，不能够被继承。

### 非访问修饰符

static 修饰符，用来修饰类方法和类变量。

final 修饰符，用来修饰类、方法和变量，final 修饰的类不能够被继承，修饰的方法不能被继承类重新定义，修饰的变量为常量，是不可修改的。

abstract 修饰符，用来创建抽象类和抽象方法。

synchronized 和 volatile 修饰符，主要用于线程的编程。



### static修饰符

静态方法不能使用类的非静态变量。



### volatile

volatile 修饰的成员变量在每次被线程访问时，都强制从共享内存中重新读取该成员变量的值。而且，当成员变量发生变化时，会强制线程将变化值回写到共享内存。这样在任何时刻，两个不同的线程总是看到某个成员变量的同一个值。



## 数据类型

整数包括byte, short, int, long, 以二进制补码表示

char类型是一个单一的16位Unicode字符

在java中使用final关键字来修饰常量

```java
final double PI = 3.1415927;
```

### 声明

```java
type identifier [ = value][, identifier [= value] ...] ;
```

## 变量



- 类变量：独立于方法之外的变量，用 static 修饰。
- 实例变量：独立于方法之外的变量，不过没有 static 修饰。
- 局部变量：类的方法中的变量。



### 局部变量

- 局部变量声明在方法、构造方法或者语句块中；
- 局部变量在方法、构造方法、或者语句块被执行的时候创建，当它们执行完成后，变量将会被销毁；
- **访问修饰符不能用于局部变量**；
- 局部变量只在声明它的方法、构造方法或者语句块中可见；
- 局部变量是在栈上分配的。
- 局部变量没有默认值，所以局部变量被声明后，**必须经过初始化**，才可以使用。

### 静态变量

- 静态变量储存在静态存储区。经常被声明为常量，很少单独使用 static 声明变量。

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

### 创建对象

对象是根据类创建的。在Java中，使用关键字 new 来创建一个新的对象。创建对象需要以下三步：

- **声明**：声明一个对象，包括对象名称和对象类型。
- **实例化**：使用关键字 new 来创建一个对象。
- **初始化**：使用 new 创建对象时，会调用构造方法初始化对象。

```java
public class Puppy{
   public Puppy(String name){
      //这个构造器仅有一个参数：name
      System.out.println("小狗的名字是 : " + name ); 
   }
   public static void main(String[] args){
      // 下面的语句将创建一个Puppy对象
      Puppy myPuppy = new Puppy( "tommy" );
   }
}
```



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