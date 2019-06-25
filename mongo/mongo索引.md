http://www.hello-code.com/blog/MongoDB/201509/5298.html


查看某个表上的所有索引
db.collection.getIndexes()

创建索引
db.collection.ensure_index([('id', 1), ('minute', 1), ('src', 1)], background=True)



options

background：是否在后台建立索引操作;
unique: 建立的索引是否唯一；
dropDups ：在建立唯一索引时是否删除重复记录；
sparse：对文档中不存在的字段数据不启用索引；这个参数需要特别注意，如果设置为true的话，在索引字段中不会查询出不包含对应字段的文档

"background"

    If you are using MongoDB version 1.3.2+, you can create indexes in the background while other operations are taking place. By default, index creation happens synchronously. If you specify TRUE with this option, index creation will be asynchronous



找到某个集合设置的索引
db.system.indexes.find({'ns': 'mobilelive.mlive_year_match_anchor_ticket_all'})