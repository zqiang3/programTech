## 1. 安装

```bash
pip install nameko
apt install rabbitmq-server
```

## 2. 入门示例

### 服务端

```python
from nameko.rpc import rpc

class HelloService(object):
    name = "hello_service"  # 服务名称

    @rpc  # 入口点标记
    def hello(self, name):
        return "hello, {}".format(name)
```

**运行服务**

```bash
nameko run helloworld
```

### 客户端

```bash
nameko shell
```

```
n.rpc.hello_service.hello(name='zq')
```



## 3. 核心概念

### 服务

一个服务就是一个python类。这个类把服务逻辑封装到方法中，而且把任何的依赖都作为方法的参数。原因很简单，微服务的核心的就是解耦。

### 进入点

进入点可以简单理解为带有@rpc标记的方法所关联的服务入口。在方法上使用了@rpc修饰的方法都将暴露给外部业务。这些进入点一般会会**监视外部事件**。例如一个**消息队列中的消息事件**，将触发进入点修饰的方法执行并返回结果。

### 依赖

* 官方提出所有非服务核心逻辑的实现最好都以依赖的形式实现。
* 依赖其实是隐藏代码的一种很好的方式。
* 使用依赖时应该把所有依赖都进行声明。

### 工作器

* 工作器就是进入点发放被触发的时候产生的微服务类实例。但是如果有依赖，那么就会被依赖的实例代替。
* 一个工作器实例只处理一次请求，提供的是无状态服务。
* 一个服务可以同时运行多个工作器，但最多只能是用户预定义的并发值。

### 依赖注入

服务类的依赖添加是声明式的。声明时不是使用接口，而是通过使用参数进行声明。 
这个参数是一个DependencyProvider。这个东西负责提供注入到服务工作器的对象。 
所有的provider都要提供get_dependency()方法生产要注入到工作器中的对象。

工作器生命周期：

1. 进入点触发
2. 通过服务类初始化工作器
3. 依赖出入到工作器
4. 执行方法
5. 工作器销毁

伪代码：

```python
worker = Service()
worker.other_rpc = worker.other_rpc.get_dependency()
worker.method()
del worker
```

依赖提供者在服务的持续时间内存活，而注入的依赖项对于每个工作器来说都是惟一的。

### 同步

Nameko基于eventlet库，这个库实现的同步模型是基于隐式yield模式的协程，通过“绿色的线程”提供同步功能。

隐式的yield基于monkey patching基础库。当一个线程等待IO时就会触发yield。通过命令==nameko run==启动的服务将会应用这个模式。

每一个工作器都有自己的线程。最大的同步工作器数量可以基于每个工作器等待IO时间的总量来动态调整。

工作器都是无状态的所以天生线程安全。但是外部依赖应该确保他们每个工作线程都是用同一个依赖或者多个工作器都能安全地同步访问。

然而c扩展体系都使用socket通信，他们通常都不认为绿色线程的工作能满足线程安全。其中就包括 librabbitmq, MySQLdb等。

### 扩展

所有的入口点和依赖提供者都作为“扩展”实现。因为他们存在于服务代码之外，又不是所有服务都需要的。（例如一个纯的AMQP暴露的服务将不会使用HTTP入口点）

Nameko有大量的内建扩展，一些是有社区提供的，而你也可以实现自己的扩展。

### 运行服务

运行服务需要的所有东西：服务类和有关的配置。 
最简单的运行一个或者多个服务的方法是使用Nameko命令行：

```bash
nameko run module:[ServiceClass]
```

这里的意思是运行某module下的所有服务或者运行某module下的特定的ServiceClass服务。



```python
from nameko.containers import ServiceContainer

class Service(object):
    name = 'service'


container = ServiceContainer(Service, config={})

service_extensions = list(container.extensions)
print 'ext', service_extensions

container.start()

container.stop()
```

## 4. 内建扩展

### RPC

Nameko包含了一个基于AMQP的RPC实现。它包括@rpc入口点，一个与其他服务对话的代理，以及一个非Nameko客户端也能发起RPC调用到集群的独立的代理

```python
# python test_rpc.py

from nameko.standalone.rpc import ClusterRpcProxy

config = {
        'AMQP_URI': 'pyamqp://guest:guest@localhost'
        }

output = ''
with ClusterRpcProxy(config) as cluster_rpc:
    output = cluster_rpc.service_x.remote_method('hello')

print 'output=', output
```



```python
# nameko run rpc   ## run service_x, service_y

from nameko.rpc import rpc, RpcProxy

class ServiceY(object):
    name = 'service_y'

    @rpc
    def append_id(self, value):
        print 'service_y rpc called'
        return u'{}-y'.format(value)


class ServiceX(object):
    name = 'service_x'

    y = RpcProxy('service_y')

    @rpc
    def remote_method(self, value):
        print 'service_x rpc called'
        res = u'{}-x'.format(value)
        return self.y.append_id(res)
```

