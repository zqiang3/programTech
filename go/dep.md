go dep 依赖管理工具是为应用管理代码的，go get是为GOPATH管理代码的



## 安装

```bash
go get -v -u github.com/golang/dep/cmd/dep
```

# 使用

## 初始化

```sh
dep init
# 更建议使用，因为会很漫长
dep init -v
```

会生成两个文件 `Gopkg.lock`、`Gopkg.toml` 和一个目录 `vendor`

> 如果报错 `Gopkg.toml and Gopkg.lock are out of sync` 需要执行一下 `dep ensure -v`

其中

- `Gopkg.toml` 是依赖管理的核心文件，可以生成也可以手动修改，[Gopkg.toml 官方文档](https://links.jianshu.com/go?to=https%3A%2F%2Fgolang.github.io%2Fdep%2Fdocs%2FGopkg.toml.html)
- `Gopkg.lock` 是生成的文件，不要手工修改 [Gopkg.lock 官方文档](https://links.jianshu.com/go?to=https%3A%2F%2Fgolang.github.io%2Fdep%2Fdocs%2FGopkg.lock.html)
- `vendor` 目录是 golang1.5 以后依赖管理目录，这个目录的依赖代码是优先加载的，类似 node 的 `node_module` 目录