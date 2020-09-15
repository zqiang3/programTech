## mac

```bash
brew install go
```



a bunch of dev tools

```bash
go get golang.org/x/tools/cmd/godoc
go get github.com/golang/lint/golint
```



## linux

### 升级

升级步骤：

1. 卸载旧版本
2. 下载新版本
3. 安装新版本
4. 配置环境变量



1. 卸载旧版本

如果是手工安装（直接复制到某个目录，如/usr/local/go），则直接删除该目录。

2. 下载

https://golang.org/dl/

3. 安装

tar zxvf go1.13.1.linux-amd64.tar.gz

mv ./go /usr/local/

4. 配置环境变量

```
export PATH="/usr/local/go/bin:$PATH"
```

如果上一个版本的路径与其相同，则不用重复添加。

路径：/usr/local/go

