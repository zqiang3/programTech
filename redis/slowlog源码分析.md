```c
#define SLOWLOG_ENTRY_MAX_ARGC 32
#define SLOWLOG_ENTRY_MAX_STRING 128

typedef struct slowlogEntry{
    robj **argv;
    int argc;
    long long id;
    long long duration;
    time_t time;
}slowlogEntry;

void slowlogInit(void);
void slowlogPushEntryIfNeeded(robj **argv, int argc, long long duration);
void slowlogCommand(redisClient *c);
```

除了两个宏定义外，slowlog.h还给出了系统内部如何保存慢日志查询的结构体slowlogEntry。除了两个宏定义外，slowlog.h还给出了系统内部如何保存慢查询日志的结构体slowlogEntry。在该结构体中，argv和argc用于保存慢查询的参数和参数个数，id就是日志的唯一Id，duration顾名思义就是该查询的执行时间，而time就是该日志被记录时的Unix时间戳。

最后，slowlog.h还声明了三个对外的函数接口。首先，slowlogInit用于初始化慢查询日志，该函数只在一个地方进行了调用，那就是初始化Redis服务器的initServer函数中。其次，slowlogPushEntryIfNeeded用于判断一条刚刚执行完的查询是否要划归为慢查询的行列，如果是就为其记录一条慢查询日志。该函数同样只在一个地方调用，那就是用于执行所有Redis命令的call函数，该函数执行完每条命令之后都会计算一下执行时间，然后调用slowlogPushEntryIfNeeded函数记录可能的慢查询日志。最后，slowlogCommand用于处理slowlog命令，它会检查slowlog命令的语法、执行命令并向客户端返回执行结果。



## slowlog.c

```c
void slowlogInit(void)
{
    server.slowlog = listCreate();
    server.slowlog_entry_id = 0;
    // 设定慢查询日志list的释放方法，用来释放list中的元素，该list中的元素也就是代码段一中给出的slowlogEntry
    listSetFreeMethod(server.slowlog, slowlogFreeEntry);
}

void slowlogFreeEntry(void *septr)
{
    slowlogEntry *se = septr;
    int j;
    for(j = 0; j < se->argc; j++)
        decrRefCount(se->argv[j]);

    zfree(se->argv);
    zfree(se);
}

void slowlogPushEntryIfNeeded(robj **argv, int argc, long long duration)
{
    if(server.slowlog_log_slower_than < 0)
        return;

    if(duration >= server.slowlog_log_slower_than)
        listAddNodeHead(server.slowlog, slowlogCreateEntry(argv, argc, durat                                                                                                                                       ion));

    while(listLength(server.slowlog) > server.slowlog_max_len)
        listDelNode(server.slowlog, listLast(server.slowlog));
}

slowlogEntry *slowlogCreateEntry(robj **argv, int argc, long long duration)
{
    slowlogFreeEntry *se = zmalloc(sizeof(*se));
    int j, slargc = argc;
    if(slargc > SLOWLOG_ENTRY_MAX_ARGC)
        slargc = SLOWLOG_ENTRY_MAX_ARGC;

    se->argc = slargc;
    se->argv = zmalloc(sizeof(robj*) * slargc);

    for(j = 0; j < slargc; j++)
    {
        if(slargc != argc && j == slargc - 1)
        {
            se->argv[j] = createOject(REDIS_STRING,
                sdscatprintf(sdsempty(), "... (%d more arguments)",
                argc-slargc+1));
        }
        else
        {
            if (argv[j]->type == REDIS_STRING &&
                argv[j]->encoding == REDIS_ENCODING_RAW &&
                sdslen(argv[j]->ptr) > SLOWLOG_ENTRY_MAX_STRING)
            {
                sds s = sdsnewlen(argv[j]->ptr, SLOWLOG_ENTRY_MAX_STRING);
                s = sdscatprintf(s, "... (%lu more bytes)",
                    (unsigned long)sdslen(argv[j]->ptr) - SLOWLOG_ENTRY_MAX_                                                                                                                                       STRING);
                se->argv[j] = createOject(REDIS_STRING, s);
            }
            else
            {
                se->argv[j] = argv[j];
                incrRefCount(argv[j]);
            }
        }
    }
    se->time = time(NULL);
    se->duration = duration;
    se->id = server.slowlog_entry_id++;
    return se;
}

void slowlogCommand(redisClient *c)
{
    if (c->argc == 2 && !strcasecmp(c->argv[1]->ptr, "reset"))
    {
        slowlogReset();
        addReply(c, shared, ok);
    }
    else if (c->argc == 2 && !strcasecmp(c->argv[1]->ptr, "len"))
    {
        addReplyLongLong(c, listLength(server.slowlog));
    }
    else if ((c->argc == 2 || c->argc == 3) &&
        !strcasecmp(c->argv[1]->ptr, "get"))
    {
        long count = 10, sent = 0;
        listIter li;
        void *totentries;
        listNode *ln;
        slowlogEntry *se;
        if (c->argc == 3 &&
            getLongFromObjectOrReply(c, c->argv[2], &count, NULL) != REDIS_O                                                                                                                                       K)
            return;

        listRewind(server.slowlog, &li);
        totentries = addDeferedMultiBulkLength(c);

        while (count-- && (ln = listNext(&li)))
        {
            int j;
            se = ln->value;
            addReplyMultiBulkLen(c, 4);
            addReplyLongLong(c, se->id);
            addReplyLongLong(c, se->time);
            addReplyLongLong(c, se->duration);
            addReplyMultiBulkLen(c, se->argc);
            for (j = 0; j < se->argc; j++)
                addReplyBuld(c, se->argv[j]);

            sent++;
        }

        setDeferredMultiBulkLength(c, totentries, sent);
    }
    else
    {
        addReplyError(c,
            "Unknown SLOWLOG subcommand or wrong # of args. Try GET, RESET,                                                                                                                                        LEN.");
    }
}

void slowlogReset(void)
{
    while (listLength(server.slowlog) > 0)
        listDelNode(server.slowlog, listLast(server.slowlog));
}
```

