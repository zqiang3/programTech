Linux chmod命令详解

chmod----改变一个或多个文件的存取模式(mode)

chmod [options] mode files

只能文件属主或特权用户才能使用该功能来改变文件存取模式。

options：
-R，--recursive
可递归遍历子目录，把修改应到目录下所有文件和子目录

作为选择，我们多数用三位八进制数字的形式来表示权限，第一位指定属主的权限，第二位指定组权限，第三位指定其他用户的权限，每位通过4(读)、2(写)、1(执行)三种数值的和来确定权限。如6(4+2)代表有读写权，7(4+2+1)有读、写和执行的权限。


实例：

$ chmod u+x file                　　　   给file的属主增加执行权限
$ chmod 751 file                　　　   给file的属主分配读、写、执行(7)的权限，给file的所在组分配读、执行(5)的权限，给其他用户分配执行(1)的权限
$ chmod u=rwx,g=rx,o=x file      上例的另一种形式
$ chmod =r file                 　　　　为所有用户分配读权限
$ chmod 444 file              　　　　 同上例
$ chmod a-wx,a+r   file   　　 　   同上例
$ chmod -R u+r directory       　   递归地给directory目录下所有文件和子目录的属主分配读的权限
$ chmod 4755                          　　设置用ID，给属主分配读、写和执行权限，给组和其他用户分配读、执行的权限。