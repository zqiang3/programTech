## 套接字

**地址家族**，**主机与端口**，**面向连接与无连接**

python只支持AF_UNIX, AF_INET, AF_NETLINK三种socket family。

AF_INET是基于网络的，所有的地址家族中，AF_INET是使用最广泛的一个。

套接字的类型有两种，一种是面向连接的套接字，这种通信方式也叫做“流套接字”，因此这种套接字的类型记为SOCK_STREAM。实现这种连接的协议主要是传输控制协议TCP。

另一种是无连接套接字，使用的是数据报协议UDP

## socket模块

```python
socket(socket_family, socket_type, protocol=0)
# 创建一个tcp套接字
tcp_sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
```

## 服务器程序

```python
# server.py
#! /usr/bin/env python
from socket import *
from time import ctime

HOST = ''
PORT = 21567
BUFSIZE = 1024
ADDR = (HOST, PORT)

tcpsock = socket(AF_INET, SOCK_STREAM)
tcpsock.bind(ADDR)
tcpsock.listen(5)


while True:
    print 'waiting for connection...'
    clisock, addr = tcpsock.accept()
    print '... connected from: ', addr

    while True:
        data = clisock.recv(BUFSIZE)
        print 'recv data = {}'.format(data)
        if not data:
            break
        content = '[%s] %s' % (ctime(), data)
        clisock.send(content)

    clisock.close()

tcpsock.close()
```

## 客户端程序

```python
# client.py
from socket import *

HOST = 'localhost'
PORT = 21567
BUFSIZE = 1024
ADDR = (HOST, PORT)

tcpsock = socket(AF_INET, SOCK_STREAM)
tcpsock.connect(ADDR)

while True:
    data = raw_input('> ')
    if not data:
        break

    tcpsock.send(data)
    data = tcpsock.recv(BUFSIZE)
    if not data:
        break

    print data

tcpsock.close()
```

