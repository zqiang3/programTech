## Gone问题

如果你用的是 go 1.13 以上的版本，那么在执行 `go get` 的时候可能会遇到这个错误

```bash
verifying code.byted.org/gopkg/logs@v1.0.0: code.byted.org/gopkg/logs@v1.0.0: reading https://sum.golang.org/lookup/code.byted.org/gopkg/logs@v1.0.0: 410 Gone
verifying code.byted.org/kite/kitutil@v3.7.4+incompatible: code.byted.org/kite/kitutil@v3.7.4+incompatible: reading https://sum.golang.org/lookup/code.byted.org/kite/kitutil@v3.7.4+incompatible: 410 Gone
```



## 解决方法

这个是 go 1.13 新有的 module proxy 引入的问题，可以参考以下方式解决.



本地/ devbox 使用

首先确保 go 版本为 **1.13 或以上**，并且开启 go mod 功能，其次更新当前 go 环境的三个配置

```bash
go env -w GOPROXY="https://go-mod-proxy.byted.org,https://goproxy.cn,https://proxy.golang.org,direct"
go env -w GOPRIVATE="*.byted.org,*.everphoto.cn,git.smartisan.com"
go env -w GOSUMDB="sum.golang.google.cn"
```



接下来参考官方文档正常使用 go 命令即可。

注意

因为代码安全性的问题，**go module proxy 并不能提供公司内仓库的代理**，参考上述设置，已经配置好了公司内仓库不走代理。因此公司内的库拉取出问题，与 go module proxy 没有关系，需要自己确定当前环境有没有访问对应 git 仓库的权限。

## 延伸阅读

- 官方介绍文章：https://blog.golang.org/using-go-modules

- 官方 wiki（内容更详细） https://github.com/golang/go/wiki/Modules

- Russ Cox 关于 go module 设计的系列博客：https://research.swtch.com/vgo