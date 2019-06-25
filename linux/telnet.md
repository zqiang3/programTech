telnet因为采用明文传送报文，安全性不好，很多Linux服务器都不开放telnet服务，而改用更安全的ssh方式了



使用netstat命令查看，TCP的23端口是否有LISTEN状态的行

DNS使用UDP协议，端口53，使用iptables-save查看



## 查看某台机器上的某个端口是否可用

telnet ip port ： 查看某一个机器上的某一个端口是否可以访问，如：telnet 114.80.67.193 8080