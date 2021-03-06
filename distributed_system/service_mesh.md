service mesh

服务网格

处理服务间通信的基础设施层，负责为构建复杂的云原生应用传递可靠的网络请求。在实践中，服务网格实现为一组和应用程序部署在一起的轻量级的网络代理，但对应用程序来说是透明的。

功能是实现请求的可靠传递

部署上体现为轻量级的网线代理

没有任何方案能一劳永逸地解决我们所有的问题

透明网络代理，从业务逻辑层抽离，作为独立的运行单元，与业务不再直接耦合

在这上面实现负载均衡、服务发现、流量调度、授权与安全控制（ACL）熔断、动态路由、安全通讯，多语言支持，多协议支持，指标和分布式追踪，请求追踪，调用链追踪

熔断：某个服务错误率太高，只能暂时停止调用

降级：按比例丢弃对依赖服务的调用

耦合性更低、灵活性更强

实现为轻量级的网络代理，通过和应用代码一起部署

与服务部署在一起，但服务无需感知，与应用部署在一起，但对应用是透明的。

上游：一个RPC调用的请求方



克服这些挑战，业界有如下三种技术方案。

- 第一种，服务自身感知服务发现、服务注册等流程，每个服务去实现相关逻辑保证服务之间协同工作正常。但是此类方案过于复杂，成本太高，每个服务都必须修改代码，难以维护。
- 第二种，通过在服务中集成服务发现、服务注册等相关功能的SDK，由SDK去完成服务治理的相关功能。SDK可以减少服务业务代码的复杂性，而且也避免了不同服务间的重复冗余的代码编写。但是SDK首先会带来语言绑定的问题，否者必须为每种语言实现对应的SDK；其次，SDK和服务绑定，所以当SDK升级时，也必须重新编译甚至适配SDK。
- 第三种，就是使用Sidecar拦截服务的进出口流量。Sidecar与服务从功能、到语言到框架都完全解耦，是两个完全独立的进程。Sidecar升级和服务更新互不影响。服务可以专注于业务功能，所有服务注册、服务发现、服务治理等能力都放置在Sidecar中实现。

作为Sidecar时，Envoy通过修改IP Table实现对服务的进出口流量的拦截，并进一步实现对进出口流量的管理。每个Sidecar通过xDS协议和控制面交互，获取集群中其他服务的相关信息以及各种服务治理相关（鉴权、分流、流量复制等等）的配置。服务本身只需要专注于业务逻辑，所有网络流量相关的工作都委托给Envoy Sidecar。