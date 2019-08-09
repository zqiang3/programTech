#!/usr/bin/env python
# coding: utf-8


import pymongo
import redis
import redis.sentinel
import json
import random
import time
import sys


app_redis_config  = {
    "host": "192.168.229.170",
    "port": 6382,
    "cluster_tag": "cluster_169-20000",
    "sentinels": [
        ["192.168.229.169", 29000],
        ["192.168.229.169", 29001],
        ["192.168.229.169", 29002],
        ["192.168.229.169", 29003]
    ],
    "socket_timeout": 5
}

app_redis_config_online =  {
    "cluster_tag": "mobile8",
    "sentinels": [
            ["10.160.179.177", 26379], ["10.160.167.5", 26379], ["10.160.110.38", 26379]
    ],
    "socket_timeout": 5,
}
app_redis_config_online =  {
    "cluster_tag": "cc_ap_mobile8",
    "sentinels": [
            ["10.170.46.33", 26379], ["10.170.47.34", 26379], ["10.170.48.34", 26379]
    ],
    "socket_timeout": 5,
}


# 数据库 redis
APP_REDIS_CONFIG = app_redis_config_online


def get_redis_client():
    f = file(sys.argv[1], 'r')
    config = json.load(f)

    sentinel_config = config['sentinel']
    sentinels_list = sentinel_config['sentinels']
    random.shuffle(sentinels_list)
    sentinel_pool = redis.sentinel.Sentinel(sentinels_list, socket_timeout=sentinel_config['socket_timeout'])
    redis_client = sentinel_pool.master_for(sentinel_config['cluster_tag'], db=0, password="")
    return redis_client

SCAN_SIZE = 10000
def get_all_redis_keys():
    all_keys = set()
    index = 0
    count = 0
    redis_cli = get_redis_client()
    while True:
        time.sleep(0.1)

        result = redis_cli.scan(index, count=SCAN_SIZE)
        index = result[0]
        all_keys.update(result[1])
        count += 1
        print '{0}: {1}'.format(count, len(result[1]))
        if index == 0:
            break

    return list(all_keys)



def main(prefix):
    redis_cli = get_redis_client()
    all_keys = get_all_redis_keys()
    count = 0
    max = (0, '')
    for key in all_keys:
        if key.startswith(prefix):
        #if 'get_videos_by_gametype_cache' in key:
            value = redis_cli.get(key)
            if value is None:
                continue
            le = len(value)
            if le > max[0]:
                max = (le, value)
            count += 1
            print key

    print max
    print 'count', count
    #data = json.loads(max[1])
    #print len(data)



if __name__ == '__main__':
    r = get_redis_client()
    print r
    prefix = sys.argv[2]
    main(prefix)
    print 'finished'


# vim: nu et ts=4 sw=4
