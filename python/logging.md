## 链接

https://www.jianshu.com/p/cad8a77762b3

http://www.cnblogs.com/BeginMan/p/3328671.html

## logging

import logging


通过logging.basicConfig函数对日志的输出格式及方式做相关配置

logging.basicConfig(level=logging.DEBUG,
​                format='%(asctime)s %(filename)s[line:%(lineno)d] %(levelname)s %(message)s',
​                datefmt='%a, %d %b %Y %H:%M:%S',
​                filename='myapp.log',
​                filemode='w')

logging.basicConfig函数各参数:
filename: 指定日志文件名
filemode: 和file函数意义相同，指定日志文件的打开模式，'w'或'a'
format: 指定输出的格式和内容，format可以输出很多有用信息，如上例所示:
 %(levelno)s: 打印日志级别的数值
 %(levelname)s: 打印日志级别名称
 %(pathname)s: 打印当前执行程序的路径，其实就是sys.argv[0]
 %(filename)s: 打印当前执行程序名
 %(funcName)s: 打印日志的当前函数
 %(lineno)d: 打印日志的当前行号
 %(asctime)s: 打印日志的时间
 %(thread)d: 打印线程ID
 %(threadName)s: 打印线程名称
 %(process)d: 打印进程ID
 %(message)s: 打印日志信息
datefmt: 指定时间格式，同time.strftime()
level: 设置日志级别，默认为logging.WARNING
stream: 指定将日志的输出流，可以指定输出到sys.stderr,sys.stdout或者文件，默认输出到sys.stderr，当stream和filename同时指定时，stream被忽略

定义一个StreamHandler，将INFO级别或更高的日志信息打印到标准错误，并将其添加到当前的日志处理对象#

console = logging.StreamHandler()
console.setLevel(logging.INFO)
formatter = logging.Formatter('%(name)-12s: %(levelname)-8s %(message)s')
console.setFormatter(formatter)
logging.getLogger('').addHandler(console)

日志一共分成5个等级，从低到高分别是：DEBUG INFO WARNING ERROR CRITICAL。这5个等级，也分别对应5种打日志的方法： debug 、info 、warning 、error 、critical。默认的是WARNING，当在WARNING或之上时才被跟踪。有两种方式记录跟踪，一种输出控制台，另一种是记录到文件中，如日志文件。

