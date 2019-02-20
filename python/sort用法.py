drive_list = [
{'uid': 20085399, 'drive_id': 1034, 'use': True, 'expire': False, 'end_time': 200000},
{'uid': 20085399, 'drive_id': 1035, 'use': False, 'expire': False, 'end_time': 300000},
{'uid': 20085399, 'drive_id': 1036, 'use': True, 'expire': True, 'end_time': 400000},
{'uid': 20085399, 'drive_id': 1037, 'use': True, 'expire': True, 'end_time': 600000},

]


drive_list = sorted(drive_list, key=lambda x: (x['use'], x['expire'], x['end_time']), reverse=True)
print drive_list

recommend_sys_data

{u'items': [{u'item_id': u'20089138', u'sub_algo': [], u'score': 0, u'game_type': 65001, u'algo': u'hot_fill'}, {u'item_id': u'20107385', u'sub_algo': [], u'score': 0, u'game_type': 9035, u'algo': u'hot_fill'}, {u'item_id': u'20889282', u'sub_algo': [], u'score': 0, u'game_type': 9050, u'algo': u'hot_fill'}, {u'item_id': u'20105715', u'sub_algo': [], u'score': 0, u'game_type': 3, u'algo': u'hot_fill'}, {u'item_id': u'21312831', u'sub_algo': [], u'score': 0, u'game_type': 9051, u'algo': u'hot_fill'}, {u'item_id': u'20106953', u'sub_algo': [], u'score': 0, u'game_type': 2, u'algo': u'hot_fill'}], u'recom_token': u'92vwXLFZaWXSOhkPxKKkKTFkhRU', u'algo_list': [u'gdbt_v2_2', u'his_type_fill', u'hot_fill'], u'flow_id': 135}