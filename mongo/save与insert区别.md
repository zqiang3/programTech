关键是'_id'字段要指定

insert仅仅是插入文档到集合中，如果记录不存在则插入，如果记录存在则忽略
save是在文档不存在时插入，存在时则是更新

在save文档的时候，如果这个文档含有"_id"键，则会调用upsert，去判断集合中是否有_id相同的文档，如果有，则更新原文档为这个所要保存的文档，否则插入该文档。

关键是'_id'字段要指定

insert仅仅是插入文档到集合中，如果记录不存在则插入，如果记录存在则忽略
save是在文档不存在时插入，存在时则是更新

在save文档的时候，如果这个文档含有"_id"键，则会调用upsert，去判断集合中是否有_id相同的文档，如果有，则更新原文档为这个所要保存的文档，否则插入该文档。