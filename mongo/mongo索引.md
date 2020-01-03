## 链接

http://www.hello-code.com/blog/MongoDB/201509/5298.html

<https://itbilu.com/database/mongo/E1tWQz4_e.html>

<https://itbilu.com/database/mongo/VJG8tei0g.html>

<https://itbilu.com/database/mongo/V1SnscdkZ.html>

## 索引相关命令

```bash
# 查看某个表上的所有索引
db.collection.getIndexes()

# 创建索引
db.COLLECTION_NAME.ensureIndex(keys[,options])

# 重建索引
db.COLLECTION_NAME.reIndex()

# 对子文档创建索引时，也可以只对某一个或几个字段创建索引：
db.users.ensureIndex({"address.city":1})

# 强制使用索引
db.users.find({name:'IT笔录', age:3}).hint({age:1})

# 删除索引
db.user.dropIndex()

找到某个集合设置的索引
db.system.indexes.find({'ns': 'mobilelive.mlive_year_match_anchor_ticket_all'})
```



options

background：是否在后台建立索引操作;
unique: 建立的索引是否唯一；
dropDups ：在建立唯一索引时是否删除重复记录；
sparse：对文档中不存在的字段数据不启用索引；这个参数需要特别注意，如果设置为true的话，在索引字段中不会查询出不包含对应字段的文档

"background"

    If you are using MongoDB version 1.3.2+, you can create indexes in the background while other operations are taking place. By default, index creation happens synchronously. If you specify TRUE with this option, index creation will be asynchronous



# Documentation

- Use [`db.collection.createIndex()`](https://docs.mongodb.com/manual/reference/method/db.collection.createIndex/#db.collection.createIndex) rather than [`db.collection.ensureIndex()`](https://docs.mongodb.com/manual/reference/method/db.collection.ensureIndex/#db.collection.ensureIndex) to create new indexes.



索引是提高查询查询效率最有效的手段。索引是一种特殊的数据结构，索引以易于遍历的形式存储了数据的部分内容（如：一个特定的字段或一组字段值），索引会按一定规则对存储值进行排序，而且索引的存储位置在内存中，所在从索引中检索数据会非常快。如果没有索引，MongoDB必须扫描集合中的每一个文档，这种扫描的效率非常低，尤其是在数据量较大时。

1. [创建／重建索引](https://itbilu.com/database/mongo/E1tWQz4_e.html#index-create)
2. [查看索引](https://itbilu.com/database/mongo/E1tWQz4_e.html#show-index)
3. [删除索引](https://itbilu.com/database/mongo/E1tWQz4_e.html#drop-index)



### 1. 创建／重建索引

MongoDB全新创建索引使用`ensureIndex()`方法，对于已存在的索引可以使用`reIndex()`进行重建。

#### 1.1 创建索引`ensureIndex()`

MongoDB创建索引使用`ensureIndex()`方法。

**语法结构**

```
db.COLLECTION_NAME.ensureIndex(keys[,options])
```

- `keys`，要建立索引的参数列表。如：`{KEY:1}`，其中`key`表示字段名，`1`表示升序排序，也可使用使用数字`-1`降序。

- `options`，可选参数，表示建立索引的设置。可选值如下：

- - `background`，Boolean，在后台建立索引，以便建立索引时不阻止其他数据库活动。默认值 false。
  - `unique`，Boolean，创建唯一索引。默认值 false。
  - `name`，String，指定索引的名称。如果未指定，MongoDB会生成一个索引字段的名称和排序顺序串联。
  - `dropDups`，Boolean，创建唯一索引时，如果出现重复删除后续出现的相同索引，只保留第一个。
  - `sparse`，Boolean，对文档中不存在的字段数据不启用索引。默认值是 false。**索引**会跳过所有不包含被**索引**键的文档。 这个**索引**之所以称为“**稀疏**” 是因为它并不包括集合中的所有文档。 与之相反，非**稀疏**的**索引**会**索引**每一篇文档，如果一篇文档不含被**索引**键则为它存储一个null值。
  - `v`，index version，索引的版本号。
  - `weights`，document，索引权重值，数值在 1 到 99,999 之间，表示该索引相对于其他索引字段的得分权重。

如，为集合`sites`建立索引：

```
> db.sites.ensureIndex({name: 1, domain: -1})
{
  "createdCollectionAutomatically" : false,
  "numIndexesBefore" : 1,
  "numIndexesAfter" : 2,
  "ok" : 1
}
```

*注意：*`1.8`版本之前创建索引使用`createIndex()`，`1.8`版本之后已移除该方法



#### 1.2 重建索引`reIndex()`

```
db.COLLECTION_NAME.reIndex()
```

如，重建集合`sites`的所有索引：

```
> db.sites.reIndex()
{
  "nIndexesWas" : 2,
  "nIndexes" : 2,
  "indexes" : [
    {
	  "key" : {
		"_id" : 1
	  },
	  "name" : "_id_",
		"ns" : "newDB.sites"
	},
	{
	  "key" : {
		"name" : 1,
		"domain" : -1
	  },
	  "name" : "name_1_domain_-1",
	  "ns" : "newDB.sites"
	}
  ],
  "ok" : 1
}
```



### 2. 查看索引

MongoDB提供了查看索引信息的方法：`getIndexes()`方法可以用来查看集合的所有索引，`totalIndexSize()`查看集合索引的总大小，`db.system.indexes.find()`查看数据库中所有索引信息。



#### 2.1 查看集合中的索引`getIndexes()`

```
db.COLLECTION_NAME.getIndexes()
```

如，查看集合`sites`中的索引：

```
>db.sites.getIndexes()
[
  {
	"v" : 1,
	"key" : {
	  "_id" : 1
	},
	"name" : "_id_",
	"ns" : "newDB.sites"
  },
  {
	"v" : 1,
	"key" : {
	  "name" : 1,
	  "domain" : -1
	},
	"name" : "name_1_domain_-1",
	"ns" : "newDB.sites"
  }
]
```



#### 2.2 查看集合中的索引大小`totalIndexSize()`

```
db.COLLECTION_NAME.totalIndexSize()
```

如，查看集合`sites`索引大小：

```
> db.sites.totalIndexSize()
16352
```



#### 2.3 查看数据库中所有索引`db.system.indexes.find()`

```
db.system.indexes.find()
```

如，当前数据库的所有索引：

```
> db.system.indexes.find()
```



### 3. 删除索引

不在需要的索引，我们可以将其删除。删除索引时，可以删除集合中的某一索引，可以删除全部索引。

#### 3.1 删除指定的索引`dropIndex()`

```
db.COLLECTION_NAME.dropIndex("INDEX-NAME")
```

如，删除集合`sites`中名为"name_1_domain_-1"的索引：

```
> db.sites.dropIndex("name_1_domain_-1")
{ "nIndexesWas" : 2, "ok" : 1 }
```



#### 3.3 删除所有索引`dropIndexes()`

```
db.COLLECTION_NAME.dropIndexes()
```

如，删除集合`sites`中所有的索引：

```
> db.sites.dropIndexes()
{
  "nIndexesWas" : 1,
  "msg" : "non-_id indexes dropped for collection",
  "ok" : 1
}
```


  几种常用索引的使用。



1. 基础索引与复合索引
   - [1.1 基础索引](https://itbilu.com/database/mongo/VJG8tei0g.html#base)
   - [1.2 组合索引](https://itbilu.com/database/mongo/VJG8tei0g.html#complex)
2. [文档索引](https://itbilu.com/database/mongo/VJG8tei0g.html#document)
3. 唯一索引与强制使用索引
   - [3.1 唯一索引](https://itbilu.com/database/mongo/VJG8tei0g.html#unique)
   - [3.2 强制使用索引](https://itbilu.com/database/mongo/VJG8tei0g.html#hint)

### 1. 基础索引与复合索引

#### 1.1 基础索引

创建索引时，可以是一个集合中的一个或多个字段。

如，为用户表`users`的`age`字段，按升序创建索引：

```
db.users.ensureIndex({age:1})
```

当数据库中有大量数据时，创建索引的操作会非常耗时，我们可以指定`backgroud:true`选项：

```
db.users.ensureIndex({age:1}, {backgroud:true})
```



#### 1.2 组合索引

为多个字段联合创建索引就是复合索引。

如，为`users`表的`age`和`city`两个字段，分别按升序和降序创建索引：

```
db.users.ensureIndex({age:1, city:-1})
```

创建复合索引后，在使用时应当注意：查询字段要在索引中存在，且顺序一致；如果索引中的首个字段没有出现在查询条件中，则不会用索引。



### 2. 文档索引

MongoDB可以为一个或多个字段创建索引，当字段是子文档时，同样可以创建索引。

如，`users`表中有以下数据：

```
{name:"IT笔录", address:{ city:"北京", district:"海淀区" }}
```

可以为`address`子文档创建索引如下：

```
db.users.ensureIndex({address:1})
```

建立索引后，查询时子文档的字段顺序要和查询顺序一致：

```
// 会使用索引
db.users.find({address:{ city:"北京", district:"海淀区" }})
// 不会使用索引
db.users.find({address:{ district:"海淀区", city:"北京" }})
```

对子文档创建索引时，也可以只对某一个或几个字段创建索引：

```
db.users.ensureIndex({"address.city":1})
```



### 3. 唯一索引与强制使用索引

#### 3.1 唯一索引

在关系型数据库中，我们可以为字段创建唯一索引，以保证字段值的唯一。在MongoDB中同样可以使用唯一索引，MongoDB创建唯一索引，在创建索引时添加`unique:true`选项即可。

如，为`users`表的`email`字段创建唯一索引：

```
db.users.ensureIndex({email:1}, {unique:true})
```

创建唯一索引后，当插入重复值时，MongoDB会报错：

```
> db.users.insert({email:'x@itbilu.com'})
WriteResult({ "nInserted" : 1 })
>
> db.users.insert({email:'x@itbilu.com'})
WriteResult({
  "nInserted" : 0,
  "writeError" : {
    "code" : 11000,
    "errmsg" : "insertDocument :: caused by :: 11000 E11000 duplicate key error index: itbilu.users.$mobile_1  dup key: { : null }"
  }
})
```



#### 3.2 强制使用索引

在MongoDB的查询中，如果查询字段中的一个或几个字段已经创建了索引，我们可以使用`hint()`函数来强制使用索引。`hint()`在查询中是非常有效的一种优化手段：

如，我们要查询`users`表中的多个字段，查询字段中的`age`字段创建过索引，可以使用`hint()`来强制傅索引查询：

```
db.users.find({name:'IT笔录', age:3}).hint({age:1})
```


  LBS（Location Based Services）定位服务，即根据用户位置查询用户附近相关信息，这一功能在很多应用上都有所使用。基于用户位置进行查询时，需要提供用户位置的经纬度。为了提高查询速度，MongoDB为坐标平面查询提供了专门的索引，称作地理空间（2d）索引。



1. [创建地理空间索引](https://itbilu.com/database/mongo/V1SnscdkZ.html#location-index-create)
2. 使用地理空间索引查询
   - [2.1 `$near`接近点查询](https://itbilu.com/database/mongo/V1SnscdkZ.html#location-index-usage-near)
   - [2.2 `$geoWithin`指定形状查询](https://itbilu.com/database/mongo/V1SnscdkZ.html#location-index-usage-within)

### 1. 创建地理空间索引

地理空间索引又称为`2d`索引。创建其它形式的索引，我们会按升序或降序（`1`或`-1`）的形式创建索引，不同于其它形式的索引，创建地理空间索引要指定的值为：`2d`。语法结构如下：

```
db.<collection>.createIndex({
  <location field> : "2d" , 
  <additional field> : <value> } ,
  { <index-specification options>})
```

- `location field`：要创建`2d`地理空间索引的字段（键）
- `additional field`：附加字段（键）
- `index-specification options`：索引选项

`index-specification options`是一个包含以下可选值的子文档：

```
{ min : <lower bound>, max : <upper bound>, bits : <bit precision> }
```

- `min bound`：{number}，最低范围，默认`-180.0`
- `min bound`：{number}，最高范围，默认`180.0`
- `bit precision`：{integer}，存储数据Geohash值精度，取值：1〜32，默认`26`



地理空间计算本质上是二维数据计算，创建索引地理空间索引时，索引键的值必须是一对值：一个包含两个数值的数组或包含两个键的内嵌文档（内嵌文档键的名称不重要）。

以下几种健值形式，都可以创建地理空间索引：

```
// 数组
{"gps": [40, 120]}
// 包含两个键的内嵌文档
{"gps": { "x":40, "y":120}}
{"gps": { "latitude":40, "longitude":120}}
```

我们可以对上面的`"gps"`健创建地理空间索引：

```
db.userlocation.ensureIndex({"gps" : "2d"}, {"min":-1000, "max":1000});  
```

这样我们就创建了地理空间索引值范围为`-1000〜1000`的索引。



### 2. 使用地理空间索引查询

#### 2.1 `$near`接近点查询

通过`$near`关键字，可以根据一个指定的平面点，按距离排序返回查询结果：

```
db.<collection>.find({ 
  <location field> :{ 
    $near : [ <x>, <y>],
    $maxDistance : <distance in meters<,
    $mixDistance : <distance in meters<
  }
})
```

- `$near`表示要查询的中心点
- `$maxDistance`距中心点的最大距离
- `$mixDistance`距中心点的最小距离

如，查询距离坐标点（40，120），10公里以内的数据：

```
db.userlocation.find({ 
  gps : { 
    $near : [40, 120],
    $maxDistance : 10
  }
})
```



#### 2.2 `$geoWithin`指定形状查询

MongoDB不仅可以按坐标点查询，还可以在查询指定形状内的文档。按形状查询使用`$geoWithin`（在`v2.4`之前使用`$within`）：

```
db.<collection<.find({ 
  <location field> :{ 
    $geoWithin : { $box|$polygon|$center : <coordinates>} 
  }
})
```

在指定形状查询中，`$box`、`$polygon`、`$center`分别表示按矩形、五边形、圆形进行查询。

如，查询坐标点为（40，120），半径为10以内的文档：

```
db.userlocation.find({ 
  gps : { 
    $geoWithin : {
      $center:[[40, 120], 10]
    }
  }
})
```



# 使用B树作索引的数据结构

如果我们使用哈希，那么对于所有单条记录查询的复杂度都会是 `O(1)`，但是遍历数据的复杂度就是 `O(n)`；如果使用 B+ 树，那么单条记录查询的复杂度是 `O(log n)`，遍历数据的复杂度就是 `O(log n) + X`，这两种不同的数据结构一种提供了最好的单记录查询性能，一种提供了最好的遍历数据的性能，但是这都不能满足 MongoDB 面对的场景 —— 单记录查询非常常见，但是对于遍历数据也需要有相对较好的性能支持，哈希这种性能表现较为极端的数据结构往往只能在简单、极端的场景下使用。

## 总结

应用场景永远都是系统设计时首先需要考虑的问题，作为 NoSQL 的 MongoDB，其目标场景就与更早的数据库就有着比较大的差异，我们来简单总结一下 MongoDB 最终选择使用 B 树的两个原因：

- MySQL 使用 B+ 树是因为数据的遍历在关系型数据库中非常常见，它经常需要处理各个表之间的关系并通过范围查询一些数据；但是 MongoDB 作为面向文档的数据库，与数据之间的关系相比，它更看重以文档为中心的组织方式，所以选择了查询单个文档性能较好的 B 树，这个选择对遍历数据的查询也可以保证可以接受的时延；
- LSM 树是一种专门用来优化写入的数据结构，它将随机写变成了顺序写显著地提高了写入性能，但是却牺牲了读的效率，这与大多数场景需要的特点是不匹配的，所以 MongoDB 最终还是选择读取性能更好的 B 树作为默认的数据结构；