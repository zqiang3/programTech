go dep 依赖管理工具是为应用管理代码的，go get是为GOPATH管理代码的



## Link

https://www.jianshu.com/p/3a4c69179a09



## 安装

```bash
go get -v -u github.com/golang/dep/cmd/dep
```

# 

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



## Usage

```bash
# 依赖管理帮助
dep help ensure
# 添加一条依赖
dep ensure -add github.com/bitly/go-simplejson
# 这里 @= 参数指定的是 某个 tag
dep ensure -add github.com/bitly/go-simplejson@=0.4.3
# 添加后，先调用一下新加入的库，然后执行 确保 同步
dep ensure
# 同理建议使用
dep ensure -v
# 更新依赖
dep ensure -update -v
#  删除没有用到的 package
dep prune -v
```

## 常见问题

### 依赖管理缓存错误

dep 的依赖管理会使用本地缓存，缓存目录是 `$GOPATH/pkg/dep/sources`
出现某些版本冲突问题时，可以删除这个缓存来解决问题

参考：**https://golang.github.io/dep/docs/failure-modes.html#bad-local-cache-state**