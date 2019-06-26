```bash
# 连接mongo
mongo host:port/dbName -u uName -p pwd

mongo 127.0.0.1:30000/cc_pt_app -upt_app_online -ppt_app_online

显示数据库列表
show dbs

显示集合列表
show collections

显示用户
show users

切换数据库
use 库名

删除当前使用的数据库
db.dropDatabase()

db.help()
use test
db.getName()
db.stats()
db.version()
db.getMongo() 当前连接的主机地址

db.getCollectionNames()

{'_id': {'$in': []}}
# $inc 
修饰器用来增加已有键的值，或者该键不存在就创建一个。
# $ne
query['day'] = {'$ne': '2016-11-29'}

# sort
# 升序
db.userInfo.find().sort({age: 1});
# python
res = mongodb[TableDef.sshow_star_info].find().sort('star_id', ASCENDING)
1代表从低到高，－1代表逆序，从高到低

# 重命名
db.foo.renameCollection( newName ) renames the collection 重命名表

# 删除索引
删除某collection的全部索引
db.collection.dropIndexes()
mongo_db[table_name].drop_indexes()

删除某个索引
db.collection.dropIndex({x: 1, y: -1})
```

### _id

_id的前四位表示时间戳



### sort

```
db.users.find().sort({"age": 1, "username": 1})
```

