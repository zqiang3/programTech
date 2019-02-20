from mongo import get_mongo_db

def clear_data(table_name):
	mongodb = get_mongo_db()
	res = mongodb[table_name].remove({})
	print res

if __name__ == '__main__':
	mongodb = get_mongo_db()
	table_name = '%s_%s' % ('errormonitor_detail_query', '2015_10_28')
	res = mongodb[table_name].aggregate({"$group": {'_id': '$keys'}})
	for doc in res['result']: 
		print doc