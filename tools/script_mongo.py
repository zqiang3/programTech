MONGO_DB = None
def get_mongo_db():
    global MONGO_DB
    try:
        if not MONGO_DB:
            app_mongo_config = CONFIG['ocean']['1']
            mongo_client = pymongo.MongoClient(app_mongo_config['ip'], int(app_mongo_config['port']), 2)
            mongo_db = mongo_client[app_mongo_config['db']]
            mongo_db.authenticate(app_mongo_config['user'], app_mongo_config['pass'])
            MONGO_DB = mongo_db
        else:
            pass
        return MONGO_DB
    except Exception, e:
        print 'connect mongo error, %s' % e
        MONGO_DB = None
        return MONGO_DB