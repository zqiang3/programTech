import pymongo

MONGO_DB = None

app_mongodb_config = {
    'ip': '192.168.229.149',
    'port': 30000,
    'db': 'gamble',
    'user': 'gamble',
    'pwd': 'gamblepwd'
}


def get_mongo_db():
    global MONGO_DB
    try:
        if not MONGO_DB:
            MONGO_CLIENT = pymongo.MongoClient(app_mongodb_config['ip'], app_mongodb_config['port'], 2)
            MONGO_DB = MONGO_CLIENT[app_mongodb_config['db']]
            MONGO_DB.authenticate(app_mongodb_config['user'], app_mongodb_config['pwd'])
        return MONGO_DB
    except Exception, e:
        print e
        MONGO_CLIENT = None
        MONGO_DB = None
        return MONGO_DB
