## Link

https://www.jianshu.com/p/598a11bbdafb



Package mock provides a system by which it is possible to mock your objects and verify calls are happening as expected.





## 安装

```bash
go get github.com/golang/mock/gomock
go get github.com/golang/mock/mockgen
go install github.com/golang/mock/mockgen # 与go get不同是？
```



## Usage

### 步骤

1. 想清楚整体逻辑
2. 定义想要依赖项的interface
3. 使用`mockgen`命令对所需的mock的interface生成mock文件
4. 编写单元测试的逻辑，在测试中使用mock
5. 进行单元测试的验证

### 接口文件

-source： 指定接口文件

-destination: 生成的文件名

-package:生成文件的包名

-imports: 依赖的需要import的包

-aux_files:接口文件不止一个文件时附加文件

-build_flags: 传递给build工具的参数

```bash
mockgen -destination spider/mock_spider.go -package spider -source spider/spider.go
```

就是将接口spider/spider.go中的接口做实现并存在 spider/mock_spider.go文件中，文件的包名为"spider"。



在我们的上面的例子中，并没有使用"-source",那是如何实现接口的呢？mockgen还支持通过反射的方式来找到对应的接口。只要在所有选项的最后增加一个包名和里面对应的类型就可以了。其他参数和上面的公用。

```bash
mockgen -destination spider/mock_spider.go -package spider github.com/cz-it/blog/blog/Go/testing/gomock/example/spider Spider
```

