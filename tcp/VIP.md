## link

https://zhaohuabing.com/post/2019-11-27-vip/#:~:text=VIP%E5%8D%B3Virtual%20IP%20Address,%E6%97%B6%E5%AF%B9%E5%AE%A2%E6%88%B7%E7%AB%AF%E7%9A%84%E5%BD%B1%E5%93%8D%E3%80%82



## 什么是VIP？

VIP是Virtual IP Address，是实现HA（高可用）系统的一种方案，高可用的目的是通过技术手段避免因为系统出现故障而导致停止对外服务，一般实现方式是部署备用服务器，在主服务器出现故障时接管业务。VIP用于向客户端提供一个固定的虚拟访问地址，以避免后端服务器发生切换时对客户端的影响。

在下面这个系统中，采用了三个服务器的集群来实现服务的高可用，后端服务器集群通过VIP 193.168.0.6对外提供服务，客户端只知道VIP，并不关注后端服务器的真实地址。

VIP被加载在Master的网卡上，所有指向VIP的请求会被发向Master，Slave服务器出于Standby状态。如果Master出现故障，集群会通过选举算法从可用的Slave节点中选出一个新的Master节点，并将VIP也迁移到新Master节点的网卡上。这样可以保证服务始终可用，并且对客户端来说访问的IP也不会变化。

VIP始终指向一个Master，因此VIP的方案并不能实现LB，只能实现HA。

## VIP的实现原理

1. Master选举：集群创建或者Master出现故障时，集群通过选举协议得到一个Master作为对外服务的节点。
2. 配置VIP：HA软件将VIP配置到Master节点的网卡上。
3. ARP广播：主动对外广播ARP消息，声明VIP对应的MAC地址为Master的网卡MAC地址。



```bash
arp -a | grep 193.168.0
```



## 采用Keepalived实现VIP



## 采用pacemaker实现VIP

