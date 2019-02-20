from mongo import get_mongo_db

def clear_data(table_name):
	mongodb = get_mongo_db()
	res = mongodb[table_name].remove({})
	print res

if __name__ == '__main__':
	clear_data('test_test')
	mongodb = get_mongo_db()
	table_name = 'test_test'
