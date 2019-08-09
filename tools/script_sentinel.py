import sys
import json

def get_redis_client(sentinel_config):
    sentinels_list = sentinel_config['sentinels']
    random.shuffle(sentinels_list)
    sentinel_pool = redis.sentinel.Sentinel(
        sentinels_list, socket_timeout=sentinel_config['socket_timeout'])
    redis_client = sentinel_pool.master_for(
        sentinel_config['cluster_tag'], db=0, password="")
    return redis_client



def main():
    if len(sys.argv) < 2:
        print 'args error'
        sys.exit(1)
        
    f = file(sys.argv[1], 'r')
    config = json.load(f)
    r = get_redis_client(config)
    print r


if __name__ == '__main__':
    main()
