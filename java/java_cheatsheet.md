## 第一个程序

```java
package com.company;

public class Main {
    public static void main(String[] args) {
        System.out.println("Hello, world");
    }
}
```

## JVM

可执行文件`javac`是编译器，可执行文件`java`是虚拟机。

Java 11新增一个功能，可以直接运行一个单文件源码。

在实际项目中，单个不依赖第三方库的Java源码是非常罕见的，所以，绝大多数情况下，我们无法直接运行一个Java源码文件，原因是它需要依赖其他的库。

**总结**

使用`javac`可以将`.java`源码编译成`.class`字节码；

使用`java`可以运行一个已编译的Java程序，参数是类名。

不推荐设置系统环境变量`classpath`，始终建议通过`-cp`命令传入。

## 类

按照惯例，类名要大写。

一个Java源码只能定义一个`public`类型的class，并且**class名称和文件名要完全一致**（这点与其他语言有明显不同）

代码的每一行以分号结尾。

`public static void main(String[] args)`是Java的固定方法入口。因此，Java程序总是从`main`方法开始执行。

`public`是访问修饰符，表示该`class`是公开的。不写public，也能正确编译，但是这个类将无法从命令行执行。`public`不仅可以修饰类，也可以修饰方法。

### 类的操作

```java
// 定义
public class Person {
  private String name;
  private int age;
}

// 创建实例
Person ming = new Person();
```

### 定义方法

```
修饰符 方法返回类型 方法名(方法参数列表) {
    若干方法语句;
    return 方法返回值;
}
```

### this变量

在方法内部，可以使用一个隐含的变量`this`，它始终指向当前实例。因此，通过`this.field`就可以访问当前实例的字段。

如果没有命名冲突，可以省略this。

### 可变参数

可变参数用`类型...`定义，可变参数相当于数组类型。

### 构造函数

**默认构造函数**：如果一个类没有定义构造方法，编译器会自动为我们生成一个默认构造方法，它没有参数，也没有执行语句。

一个构造方法可以调用其他构造方法，便于代码复用。

在Java中，创建对象实例的时候，按照如下顺序进行初始化：

1. 先初始化字段，例如，`int age = 10;`表示字段初始化为`10`，`double salary;`表示字段默认初始化为`0`，`String name;`表示引用类型字段默认初始化为`null`；
2. 执行构造方法的代码进行初始化。

### 方法重载

方法名相同，但参数各不相同。

例如：`String`类提供了多个重载方法`indexOf()`，可以查找子串：

- `int indexOf(int ch)`：根据字符的Unicode码查找；
- `int indexOf(String str)`：根据字符串查找；
- `int indexOf(int ch, int fromIndex)`：根据字符查找，但指定起始位置；
- `int indexOf(String str, int fromIndex)`根据字符串查找，但指定起始位置。



### 继承

当子类继承父类时，就获得了父类的所有功能。

Java使用`extends`关键字来实现继承。

在Java中，没有明确写`extends`的类，编译器会自动加上`extends Object`。

java中只允许单继承。

继承有个特点，就是子类无法访问父类的`private`字段或者`private`方法。用`protected`修饰的字段可以被子类访问。一个`protected`字段和方法可以被其子类，以及子类的子类所访问。

```java
class Student extends Person {
  private int score;
  
  public int getScore() {...}
  public void setScore(int score) {...}
}
```



子类的构造方法不能从基类继承，而是编译器自动生成的。编译器自动生成的构造方法在第一行语句使用`super()`调用父类的构造方法。

**阻止继承**

在类加上修饰符`final`，那么其他类不能再继承此类。

从Java 15开始，允许`sealed`修改class，并通过`permits`明确写出从该class继承的子类名称。

**向上转型**

把一个子类类型安全地变为父类类型的赋值，被称为向上转型（upcasting）。

例如，类`Student`继承自`Person`，下面的代码是合法的。

```java
Person p = new Person();
Person p = new Student();
```

继承树是`Student > Person > Object`，所以，可以把`Student`类型转型为`Person`，或者更高层次的`Object`。

**向下转型**

和向上转型相反，如果把一个父类类型强制转型为子类类型，就是向下转型（downcasting）。

```java
Person p1 = new Student(); // upcasting, ok
Person p2 = new Person();
Student s1 = (Student) p1; // ok
Student s2 = (Student) p2; // runtime error! ClassCastException!
```

Java提供了`instanceof`操作符，可以先判断一个实例究竟是不是某种类型

利用`instance`，在向下转型前可以先进行判断，确保安全地进行转型。

```java
if (p instance Student) {
  Student s;
  s = (Student) p;
}
```



**小结**

- 继承是面向对象编程的一种强大的代码复用方式；
- Java只允许单继承，所有类最终的根类是`Object`；
- `protected`允许子类访问父类的字段和方法；
- 子类的构造方法可以通过`super()`调用父类的构造方法；
- 可以安全地向上转型为更抽象的类型；
- 可以强制向下转型，最好借助`instanceof`判断；
- 子类和父类的关系是is，has关系不能用继承。



### 多态

Java的实例方法调用是基于运行时的实际类型的动态调用，而非变量的声明类型。

多态是指，针对某个类型的方法调用，其真正执行的方法取决于运行时期实际类型的方法。

在子类的覆写方法中，如果要调用父类的被覆写的方法，可以通过`super`来调用。

用`final`修饰的方法不能被`Override`。

对于一个类的实例字段，同样可以用`final`修饰。用`final`修饰的字段在初始化后不能被修改。

可以在构造方法中初始化final字段：

```java
class Person {
  public final String name;
  public Person(String name) {
    this.name = name;
  }
}
```

### 抽象类和抽象方法

使用`abstract`可以把一个方法定义为抽象方法，抽象方法没有提供任何实现语句，因为这个方法是不能被执行的，包含抽象方法的类也是无法被实例化，必须也将类也定义为`abstract`。

如果不实现抽象方法，则子类仍是一个抽象类。

```java
abstract class Person {
  public abstract void run();
}
```

无法实例化的抽象类有什么用？

因为抽象类本身被设计成只能用于被继承，因此，抽象类可以强迫子类实现其定义的抽象方法，否则编译会报错。因此，抽象方法实际上相当于定义了“规范”。

**面向抽象**编程

这种尽量引用高层类型，避免引用实际子类型的方式，称之为面向抽象编程。

### 接口

如果一个抽象类没有字段，所有方法全部都是抽象方法，就可以把抽象类改写为接口。

在Java中，使用`interface`可以声明一个接口：

```java
interface Person {
  void run();
  String getName();
}
```

接口定义的所有方法默认都是`public abstract`的。

当一个具体的`class`去实现一个`interface`时，需要使用`implements`关键字。

一个类可以实现多个`interface`。

一个`interface`可以继承自另一个`interface`。`interface`继承自`interface`使用`extends`。

在使用的时候，实例化的对象永远只能是某个具体的子类，但总是通过接口去引用它，因为接口比抽象类更抽象。

**default方法**

在接口中，可以定义`default`方法。例如，把`Person`接口的`run()`方法改为`default`方法。

`default`方法的目的是，当我们需要给接口新增一个方法时，会涉及到修改全部子类。如果新增的是`default`方法，那么子类就不必全部修改，只需要在需要覆写的地方去覆写新增方法。

**小结**

Java的接口（interface）定义了纯抽象规范，一个类可以实现多个接口；

接口也是数据类型，适用于向上转型和向下转型；

接口的所有方法都是抽象方法，接口不能定义实例字段；

接口可以定义`default`方法（JDK>=1.8）。



### 静态字段和静态方法

使用`static`修饰符修饰后，一个字段就成为静态字段。静态字段属于类，所有实例共享一个静态字段。

不推荐用`实例变量.静态字段`去访问静态字段，因为在Java程序中，实例对象并没有静态字段。在代码中，实例对象能访问静态字段只是因为编译器可以根据实例类型自动转换为`类名.静态字段`来访问静态对象。

用`static`修饰的方法称为静态方法。静态方法类似其它编程语言的函数。

因为静态方法属于`class`而不属于实例，因此，静态方法内部，无法访问`this`变量，也无法访问实例字段，它只能访问静态字段。

通过实例变量也可以调用静态方法，但这只是编译器自动帮我们把实例改写成类名而已。

因为`interface`是一个纯抽象类，所以它不能定义实例字段。但是，`interface`是可以有静态字段的，并且静态字段必须为`final`类型

### 包和作用域

不用`public`、`protected`、`private`修饰的字段和方法就是包作用域。

`public`, `protected`, `private`。

Java支持嵌套类，嵌套类拥有访问`private`的权限。

包作用域：包作用域是指一个类允许访问同一个`package`的没有`public`、`private`修饰的`class`，以及没有`public`、`protected`、`private`修饰的字段和方法。

一个`.java`文件只能包含一个`public`类，但可以包含多个非`public`类。如果有`public`类，文件名必须和`public`类的名字相同。

## 数据类型

计算机内存的最小存储单元是字节（byte），一个字节就是一个8位二进制数，即8个bit。它的二进制表示范围从`00000000`~`11111111`，换算成十进制是0~255，换算成十六进制是`00`~`ff`。

一个字节是1byte，1024字节是1K，1024K是1M，1024M是1G，1024G是1T。

java的char类型占用2个byte。

**各种整形范围**

- byte：-128 ~ 127
- short: -32768 ~ 32767
- int: -2147483648 ~ 2147483647
- long: -9223372036854775808 ~ 9223372036854775807



### float

表示`float`类型时，需要加上`f`。

### 引用类型

除了基本类型，都是引用类型。

引用类型的默认值是`null`。

### 常量

加上`final`修饰符，就定义了常量。

### 字符和字符串

Java在内存中总是使用Unicode表示字符，要显示一个字符的Unicode编码，只需将`char`类型直接赋值给`int`类型即可。

还可以直接用转义字符`\u`+Unicode编码来表示一个字符

```java
char a = '\u0041';
```

**转义字符**

常见的转义字符包括：

- `\"` 表示字符`"`
- `\'` 表示字符`'`
- `\\` 表示字符`\`
- `\n` 表示换行符
- `\r` 表示回车符
- `\t` 表示Tab
- `\u####` 表示一个Unicode编码的字符



**字符串连接**

可以使用`+`连接字符串和任意数据类型。

如果用`+`连接字符串和其他数据类型，会将其他数据类型先自动转型为字符串，再连接



**多行字符串**

```java
String s = """
  SELECT * FROM
    users 
  WHERE id > 100
  ORDER BY name DESC
  """;
```

多行字符串前面共同的空格会被去掉

Java的字符串还有个重要特点，就是字符串不可变。



### 数组

```java
int[] ns = new int[5];
int len = ns.length;

// 另一种初始化方法，由编译器自动推算数组大小。
int[] ns = new int[] {1, 2, 3};
int[] ns = {1, 2, 3};
```

可变性

```java
int[] ns;
ns = new int[] {1, 2, 3, 4, 5};
ns = new int[] {1, 2, 3};
```

数组元素可以是值类型（如int）或引用类型（如String），但数组本身是引用类型；



**二维数组**

二维数组就是数组的数组，二维数组的每个数组元素的长度并不要求相同

```java
public class Main {
    public static void main(String[] args) {
        int[][] ns = {
            { 1, 2, 3, 4 },
            { 5, 6, 7, 8 },
            { 9, 10, 11, 12 }
        };
        System.out.println(ns.length); // 3
    }
}
```

**三维数组**

三维数组就是二维数组的数组。

```java
int[][][] ns = {
    {
        {1, 2, 3},
        {4, 5, 6},
        {7, 8, 9}
    },
    {
        {10, 11},
        {12, 13}
    },
    {
        {14, 15, 16},
        {17, 18}
    }
};
```

**多维数组**

理论上，我们可以定义任意的N维数组。但在实际应用中，除了二维数组在某些时候还能用得上，更高维度的数组很少使用。



### var

使用`var`可省略书写变量类型，此时编译器会自动推动变量类型。

```java
stringBuilder sb = new StringBuilder();
var sb = new StringBuilder(); // 跟go的写法有些像
```



### 空值null

引用类型的变量可以指向一个空值`null`，它表示不存在，变量不指向任何对象。



## 数据运算

除数为0时编译时不会报错，运行时才报错。

计算结果超出范围时会产生溢出，溢出不会报异常，却会得到一个奇怪的结果。

### 移位运算

对负数进行右移，最高位不动，因此结果仍是一个负数。

还有一种无符号的右移运算，使用`>>>`，它的特点是不管符号位，右移后高位总是补`0`，因此，对一个负数进行`>>>`右移，它会变成正数，原因是最高位的`1`变成了`0`。

对`byte`和`short`进行移位时，会首先转换为`int`再进行移位。

### 运算优先级

- `()`
- `!` `~` `++` `--`
- `*` `/` `%`
- `+` `-`
- `<<` `>>` `>>>`
- `&`
- `|`
- `+=` `-=` `*=` `/=`

### 类型自动提升

go语言在这点上不同，参与运算的类型必须是一模一样的。



### 浮点数运算

浮点数`0.1`在计算机中就无法精确表示，因为十进制的`0.1`换算成二进制是一个无限循环小数。但是，`0.5`这个浮点数又可以精确地表示。

整型和浮点型运算时，整型会自动提升为浮点型。

整数运算在除数为0时会报错，而浮点数运算在除数为0时不会报错，会返回几个特殊值。

- `NaN`表示Not a Number
- `Infinity`表示无穷大
- `-Infinity`表示负无穷大

### 布尔运算

布尔运算是一种关系运算，包括以下几类：

- 比较运算符：`>`，`>=`，`<`，`<=`，`==`，`!=`
- 与运算 `&&`
- 或运算 `||`
- 非运算 `!`

关系运算符的优先级从高到低依次是：

- `!`
- `>`，`>=`，`<`，`<=`
- `==`，`!=`
- `&&`
- `||`

### 短路运算



### 三元运算符

```java
b ? x : y
```

注意到三元运算`b ? x : y`会首先计算`b`，如果`b`为`true`，则只计算`x`，否则，只计算`y`。此外，`x`和`y`的类型必须相同，因为返回值不是`boolean`，而是`x`和`y`之一。



## 格式化输出

格式化输出使用`System.out.printf()`，通过使用占位符`%?`

格式化占位符

| 占位符 | 说明                             |
| :----- | :------------------------------- |
| %d     | 格式化输出整数                   |
| %x     | 格式化输出十六进制整数           |
| %f     | 格式化输出浮点数                 |
| %e     | 格式化输出科学计数法表示的浮点数 |
| %s     | 格式化字符串                     |

注意，由于%表示占位符，因此，连续两个%%表示一个%字符本身。

参考  [java.util.Formatter](https://docs.oracle.com/en/java/javase/11/docs/api/java.base/java/util/Formatter.html#syntax)





## 流程控制

### if判断

**语法**

```
if (条件) {
    // 条件满足时执行
}
```

还可以用多个`if ... else if ...`串联

```java
public class Main {
    public static void main(String[] args) {
        int n = 70;
        if (n >= 90) {
            System.out.println("优秀");
        } else if (n >= 60) {
            System.out.println("及格了");
        } else {
            System.out.println("挂科了");
        }
        System.out.println("END");
    }
}
```

判断引用类型是否相等

`==`表示是否指向同一个对象，要判断内容是否相等，可以使用`equals()`方法。



### switch

```java
package com.company;

public class Main {
    public static void main(String[] args) {
        int i = 10;
        switch (i) {
            case 1:
                System.out.println(1);
                break;
            case 2:
                System.out.println(2);
                break;
            default:
                System.out.println("default");
        }

    }
}
```

`switch`语句具有穿透性，漏写break会导致意外结果。

switch还可以使用字符串。

switch的计算结果必须是整型，字符串和枚举类型。



### while

```java
while (condition) {
  ...
}
```

### do while

```java
do {
  
} while (condition);
```

### for

```java
for (int i = 0; i < 100; i++) {
  ...
}
```

避免在循环体内修改计数器的值！

### for each

```java
int[] ns = {1, 4, 9, 16, 25}
for (int n : ns) {
  System.out.println(n);
}
```

`for each`可以遍历所有“可迭代”的数据类型。

### continue break

`break`语句可以跳出当前循环；

`break`语句总是跳出最近的一层循环；

`continue`语句可以提前结束本次循环；