a UDP client can create a socket and send a datagram to a given server and then immediately send another datagram on the same socket to a different server. Similarly, a UDP server can receive several datagrams on a single UDP socket, each from a different client.



TCP provides connection

give every byte a sequence number

一个TCP包如果被拆分为两段，如果在接收段是乱序收到的话，会先按sequence number重新组合



从可靠性的角度分析：UDP没有确认机制

不可靠：包可能丢失，可能重复，可能乱序



TCP flow control, advertised window



没有flow control

发送端可以疯狂发，超出服务端处理能力



四次挥手

什么时候开始发送FIN包？

调用close

进程终止

main退出