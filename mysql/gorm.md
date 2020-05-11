```




```

`github.com/jinzhu/gorm/dialects/mysql` 是 golang 的 mysql 驱动，实际上就是 `github.com/go-sql-driver/mysql` 作者这里为了好记，重新弄了个名字



## 为什么我不用gorm？

如果大家写Golang有点时日，很有可能听说过https://github.com/jinzhu/gorm，一个非常有名的Golang的ORM库。我自己是不用的，一来是不会用选择用Golang做CURD开发，吃力不讨好；二来是我觉得gorm的API设计很糟糕。

写一个ORM库是很困难的，不但要对不同的关系数据库特性有高度归纳能力，而且要对所使用的语言有深入的理解。ORM是这两种不同专业领域之间的桥梁，其复杂性可想而知。

可能是因为实现难度高，Golang下一直没有比较好用的ORM库。要么是直接使用官方的 https://golang.org/pkg/database/sql/ ，要么是用简单的上层建筑如 https://github.com/jmoiron/sqlx 或某种QueryBuilder如https://github.com/gocraft/dbr。这些库都各有优点，但抽象能力都远不如Rails里的ActiveRecord或者Python里的SQLAlchemy，在这种背景下gorm就显得鹤立鸡群：又能关联表，又能eager load，官人要啥就实现啥。

可惜的是，ORM是个硬骨头，gorm想做的很多，但能力却没跟上。

ORM是复杂的。gorm最大的问题，就是试图对复杂的问题抽象却没法给出完美的方案。这让我想起我学习Rust时印象最深刻的关于字符串的一节：

> Rust has chosen to make the correct handling of `String` data the default behavior for all Rust programs, which means programmers have to put more thought into handling UTF-8 data upfront. This trade-off exposes more of the complexity of strings than is apparent in other programming languages, but it prevents you from having to handle errors involving non-ASCII characters later in your development life cycle.
>
> [https://doc.rust-lang.org/book/ch08-02-strings.html#strings-are-not-so-simple﻿](https://doc.rust-lang.org/book/ch08-02-strings.html#strings-are-not-so-simple)

字符串处理的本质是复杂的，Rust在设计这部分的API的时候，刻意选择了暴露其复杂性，而不是隐藏细节。这虽然增加了开发者的学习成本，但收益是更高的软件质量。

而官方库及其他的上面提及的库其实也反应了类似的思想：只要开发者对数据库有一定的理解，就能想像出每个API背后生成的SQL。这种API的结果是准确的可预测的，可能不方便，但不会让开发者产生困扰。

而gorm选择的是最大限度的抽象，提供的是一个大而全的*DB*对象，用一种类似Chaining的设计，几乎所有的API都调用它，而它所有的结果都返回它。它是不可知的，你不知道你的数据从哪里来，到哪里去，发生了什么事。 gorm的作者试图用黑魔法把关系数据库的细节都隐藏起来让傻瓜都能用，然而傻瓜根本就不应该用数据库。

gorm的这种设计显然违背了单一功能原则（Single responsibility principle）。我们看回去官方的API：*DB*的*Conn*方法返回*Conn*，*Conn*调用*Begin*返回*Tx*，*Tx*调用*Query*可以返回*Rows*，*Rows*可以查看结果，可以查看错误。每个结构体都只有最低限度的功能，但是只要一看文档就能知道要用什么方法生成什么，一目了然。

黑魔法是很危险的，就算优秀设计如ActiveRecord，用不好一样会出N+1问题。gorm的这种设计更危险，你不知道哪个方法会返回错误，哪个方法不会。这种缺乏一致性的设计让开发者困扰，也违反了Golang对错误处理的最佳实践，一不小心就会出bug。

gorm的这种设计导致的另一个问题是：你要弥补设计上的问题，不能改API，那只能牺牲性能。比如说你打算用goroutine同时Update两个表，因为返回的都是**DB*类型，你会很困惑到底是不是同一个实例，结果里的Error会不会有race condition问题。于是你打开源码一看，发现gorm好样的，它会给你自动clone一份。你又看了一下其他代码，好样的，不管有没用，居然全给你clone了。

gorm还有一些不大不小的问题，就按下不表了。自己也不想对开源代码太苛刻，毕竟谁没写过烂代码？最后介绍一本书，总结了很多Golang下的设计模式，共勉。