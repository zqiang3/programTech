传统的[Sendmail](https://www.centos.bz/category/email/sendmail/)将所有功能都集中在同一个程序里，这种结构我们称之为“单体式设计”(monolithic).[Postfix](https://www.centos.bz/category/email/postfix/)采用专职负责的策略，不同的功能分别交由不同的专门程序处理，这种结构称为“模块化设计”(modular)。

当Postfix被启动后，首先启动的是[master](https://www.centos.bz/tag/master/) daemon，它主导邮件的处理流程，同时也是其他组件的总管。在处理邮件的过程中，master会启动对应功能的组件来处理相关事宜，被master启动的组件，在完成交付的工作之后会自行结束；或者，如果组件的处理时间超过时限，或是工作量到达预定限度，组件也会自行结束。master daemon会常驻在系统中，当管理员启动它时，它从main.cf和master.cf这两个配置文件取得启动参数。

### 组件结构

　　Master组件：主导邮件处理流程、其他组件的总管。配置文件：main.cf和master.cf。
　　Qmgr组件：队列管理器。各个postfix组件之间的合作依靠队列交换邮件。
　　Sendmail组件：服务器本机发送邮件。
　　Postdrop组件：将邮件存入postfix队列目录下的maildrop/子目录。
　　Pickup组件：监视maildrop/子目录，读出新邮件，交给cleanup组件。
　　Cleanup组件：补足遗漏的标头字段。
　　Trivial-Rewrite组件：地址处理，改成标准格式。决定路由信息，包括传输方法、下一站以及收件人地址。
　　Smtpd组件：接收来自网络的邮件，交给cleanup组件处理。
　　Defer组件：邮件被延时时产生通知函。
　　Bounce组件：邮件无法送达目的地时产生通知函。
　　Dns组件：查找符合条件的邮件服务器。

### Postfix命令行工具

　　postalias：创建或查询别名数据库。
　　postcat：显示出队列文件的内容，让管理员可观察滞留在队列里的邮件内容。
　　postconf：显示或改变postfix参数，可一次显示一个参数，或是显示所有参数。
　　postdrop：将邮件放回到maildrop目录，由postfix重新进行投递操作。
　　postfix：启动或停止postfix系统，或重新读取配置文件。也可以用于其他维护工作，包括检查系统配置，以及清空队列。
　　postkick：对特定postfix服务发出请求。此工具的作用，主要是给shell scripts提供一个能够与postfix沟通服务的管道。
　　postlock：锁定特定文件，确保能够独占访问。此工具的作用，主要是让shell scripts能使用兼容于postfix的锁定方式。
　　postlog：将特定的信息记录到系统日志文件中。这是支持shell scripts工具，使其能以类似于postfix的样式来记录信息到日志文件。
　　postmap：创建查询表的DB数据库或查询查询表内容。postfix有许多配置信息都是记录在postmap所建的查询表数据库中。
　　postqueue：让一般的用户能够有限度地访问postfix队列。可能改变队列的访问方式需要有管理员特权才能进行，而这方面的访问能力由postsuper命令提供。
　　postsuper：供管理员访问postfix队列。管理员可删除邮件、扣留邮件(搬到hold队列)、取回邮件(将邮件从hold队列搬回active队列)，必要时，还可以修复队列目录结构。