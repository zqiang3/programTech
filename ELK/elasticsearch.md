## 链接

https://blog.csdn.net/makang110/article/details/80596017

https://blog.csdn.net/laoyang360/article/details/52227541

## 介绍

近年ElasticSearch发展迅猛，已经超越了其最初的纯搜索引擎的角色，现在已经增加了数据聚合分析（aggregation）和可视化的特性，如果你有数百万的文档需要通过关键词进行定位时，ElasticSearch肯定是最佳选择。当然，如果你的文档是JSON的，你也可以把ElasticSearch当作一种“NoSQL数据库”， 应用ElasticSearch数据聚合分析（aggregation）的特性，针对数据进行多维度的分析。

【知乎：热酷架构师潘飞】ES在某些场景下替代传统DB 
个人以为Elasticsearch作为内部存储来说还是不错的，效率也基本能够满足，在某些方面替代传统DB也是可以的，前提是你的业务不对操作的事性务有特殊要求；而权限管理也不用那么细，因为ES的权限这块还不完善。 
由于我们对ES的应用场景仅仅是在于对某段时间内的数据聚合操作，没有大量的单文档请求（比如通过userid来找到一个用户的文档，类似于NoSQL的应用场景），所以能否替代NoSQL还需要各位自己的测试。 
如果让我选择的话，我会尝试使用ES来替代传统的NoSQL，因为它的横向扩展机制太方便了。

## ES国内外使用优秀案例

1） 2013年初，GitHub抛弃了Solr，采取ElasticSearch 来做PB级的搜索。 “GitHub使用ElasticSearch搜索20TB的数据，包括13亿文件和1300亿行代码”。

2）维基百科：启动以elasticsearch为基础的核心搜索架构。 
3）SoundCloud：“SoundCloud使用ElasticSearch为1.8亿用户提供即时而精准的音乐搜索服务”。 
4）百度：百度目前广泛使用ElasticSearch作为文本数据分析，采集百度所有服务器上的各类指标数据及用户自定义数据，通过对各种数据进行多维分析展示，辅助定位分析实例异常或业务层面异常。目前覆盖百度内部20多个业务线（包括casio、云分析、网盟、预测、文库、直达号、钱包、风控等），单集群最大100台机器，200个ES节点，每天导入30TB+数据。

## 一线公司ES使用场景：

1）新浪ES 如何分析处理32亿条实时日志 <http://dockone.io/article/505> 
2）阿里ES 构建挖财自己的日志采集和分析体系 <http://afoo.me/columns/tec/logging-platform-spec.html> 
3）有赞ES 业务日志处理 <http://tech.youzan.com/you-zan-tong-ri-zhi-ping-tai-chu-tan/> 
4）ES实现站内搜索 <http://www.wtoutiao.com/p/13bkqiZ.html>

## ES部署（无需安装）

1）零配置，开箱即用 
2）没有繁琐的安装配置 
3）java版本要求：最低1.7 
我使用的1.8 
[root@laoyang config_lhy]# echo $JAVA_HOME 
/usr/java/jdk1.8.0_201 
4）下载地址： 
5）启动 
cd /usr/local/elasticsearch-2.3.5 

/home/ops/source/elasticsearch-6.5.4

./bin/elasticsearch 
bin/elasticsearch -d(后台运行)

## ES windows下一键安装

自写bat脚本实现windows下一键安装。 
1）一键安装ES及必要插件（head、kibana、IK、logstash等） 
2）安装后以服务形式运行ES。 
3）比自己摸索安装节省至少2小时时间，效率非常高。 
脚本说明： 
<http://blog.csdn.net/laoyang360/article/details/51900235>

## ES必要的插件

必要的Head、kibana、IK（中文分词）、graph等插件的详细安装和使用。 
<http://blog.csdn.net/column/details/deep-elasticsearch.html>

## ES对外接口（开发人员关注）

**JAVA API**

<http://www.ibm.com/developerworks/library/j-use-elasticsearch-java-apps/index.html>

**RESTful API**

常见的增、删、改、查操作实现： 
<http://blog.csdn.net/laoyang360/article/details/51931981>

## ES遇到问题怎么办？

1）国外：<https://discuss.elastic.co/> 
2）国内：<http://elasticsearch.cn/>

# 参考：

[1] http://www.tuicool.com/articles/7fueUbb 
[2] http://zhaoyanblog.com/archives/495.html 
[3]《Elasticsearch服务器开发》 
[4]《实战Elasticsearch、Logstash、Kibana》 
[5]《Elasticsearch In Action》 
[6]《某ES大牛PPT》

## 数据库操作

```bash
curl -H "Content-Type: application/json" localhost:9200/test_index_1221/test_type/5 -d '{"user_name":"xiaoming"}'
>>>{"_index":"test_index_1221","_type":"test_type","_id":"5","_version":1,"result":"created","_shards":{"total":2,"successful":1,"failed":0},"_seq_no":0,"_primary_term":1}
```

## 查询

使用 [Match 查询](https://www.elastic.co/guide/en/elasticsearch/reference/5.5/query-dsl-match-query.html)，指定的匹配条件是`desc`字段里面包含"软件"这个词

```bash
$ curl 'localhost:9200/accounts/person/_search'  -d '
{
  "query" : { "match" : { "desc" : "软件" }}
}'
```

使用python脚本

```python
url = 'http://47.107.234.148/accounts/person/_search'
h = {
    "Content-Type": "application/json"
}
d = {
    "query": {'match': {'user': 'zhang wang'}},  # zhang or wang
    "size": 100,  # 默认是10
    "from": 1,    # 指定位移
}
print json.dumps(d)
r = requests.post(url, data=json.dumps(d), headers=h)
print r.json()
```

## python开发

```python
pip install elasticsearch	
```

## 性能测试工具

rally