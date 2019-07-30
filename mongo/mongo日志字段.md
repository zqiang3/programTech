| 字段名          | 字段含义                                                     |
| --------------- | ------------------------------------------------------------ |
| @timestamp      | 日志处理（生成）的时间                                       |
| _id             | 日志在elk中的编号                                            |
| collection      | mongodb操作的collection名                                    |
| command         | mongodb操作类型：insert、query、update、remove、getmore 、findAndModify等等 |
| connid          | mongodb客户端连接的id编号                                    |
| content         | mongodb具体操作的内容，例如更新、删除数据的内容（不包含查询条件） |
| database        | mongodb操作的数据库名                                        |
| duration        | mongodb操作的耗时，此为慢日志最关键的指标，反应了mongodb从收到操作到返回的耗时时间 |
| find            | findAndModify对应的find操作内容                              |
| keyUpdates      | 索引键变更的数量                                             |
| modify          | findAndModify对应的modify操作内容                            |
| nMatched        | update、findAndModify等操作中的查询条件匹配的doc条数         |
| nModified       | update、findAndModify等操作中被修改的doc条数                 |
| ndeleted        | 被删除的doc条数                                              |
| nreturned       | 操作返回的doc条数                                            |
| nscanned        | 从索引中扫描的doc条数                                        |
| nscannedObjects | collection中扫描的doc条数                                    |
| ntoreturn       | 操作返回的doc条数: 如果nscanned远大于nreturned的话，考虑添加索引来优化 |
| ntoskip         | 使用skip()方法跳过的doc条数                                  |
| numYields       | 操作被yield的次数，例如在数据不在内存中需要等待IO            |
| ordered         | 操作的结果是无序的doc，需要在内存中排序后才能返回结果        |
| query           | 查询或更新操作中的查询内容                                   |
| reslen          | 操作结果返回的内容长度（单位：字节），太多的返回会影响性能   |
| source_host     | 产生日志的ocean mongodb节点的ip                              |
| update          | update操作的内容                                             |
| update_num      | update操作的条数                                             |
| upsert          | 是否产生了upsert操作                                         |
| writeConcern    | 操作的writeConcern设置                                       |
| writeConflicts  | 产生写操作冲突的次数，例如并发update同一条doc                |

### discover

如果用户想要直接进行某个field的查询，可以在Discover页面中的搜索栏进行操作

- 比如说用户想要全文查询某个字符串，可以直接在搜索栏中查询，查询支持*和?通配符，不支持其它正则表达式

- 要查询具体的某个字段： 可使用"字段名:查询内容"的方式来查询: 如 `project:xx`
- 组合查询，支持AND和OR这样的查询表达式，例如：单个查询条件 and 单个查询条件 or 单个查询条件，如 `project:xx AND command:update`

### dashboard

- Dashboard页面展示了在ELK中通过一定的过滤规则得到的统计信息。这些规则包含了常用的聚合查询功能，可以对ELK中的每个字段进行统计分析。
- 图表展示比较直观，可以直接观察到一段时间内的各个域的统计情况，进一步帮助用户分析mongo日志以调整优化服务应用。



目前我们在 dashboard 页面中提供了两类图表展示：

- 慢日志耗时分布

  慢日志根据消耗时间按0~300ms, 300~800ms, 800~2000ms, 2000~5000ms, 5000ms~ 这5个段做统计，每个段包含的条数展示成图表放到dashboard中

- 慢日志对应的操作类型分布

  - 根据慢日志的操作类型来分类统计，主要包含了query、update、delete、remove、insert、findAndModify 这6种操作类型分别统计日志条数并展示

- 慢日志具体信息详情

  在图表下方直接显示了相关的慢日志具体操作情况，在搜索框中进行搜索过滤时，该部分内容也会同步调整变更。