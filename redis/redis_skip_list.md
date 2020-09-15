## 数据结构

```
typedef struct zskiplist {
	struct zskiplistNode *header, *tail;
	unsigned long length;
	int level;
} zskiplist;

typedef struct zskiplistNode {
	robj *obj;
	double score;
	struct zskiplistNode *backward;
	struct zskiplistLevel {
		struct zskiplistNode *forward;
		unsigned int span;
	} level[];
} zskiplistNode;
```

