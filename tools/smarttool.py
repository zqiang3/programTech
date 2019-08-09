#!/usr/bin/env python
# coding: utf-8

import json
import wrapt
import sys
import requests
from itertools import izip
from logger import Log


def smart_batch(redis_key_prefix, redis_ttl, Log,
                redis_client=None, default_value={}, max_size=0):
    """
    :author: gzzhangqiang2014@corp.netease.com
    :param redis_client:     redis client
    :param redis_key_prefix: redis键前缀, 末尾自动补充'%s'
    :param ttl:              redis expire time
    :param default_value:    默认值
    :param max_size:         每次操作的最大值
    :return:                 包装函数
    """
    def redis_mget(redis_cli, key_prefix, keys):
        """redis mget"""
        cache_keys = [key_prefix % key for key in keys]
        cache_values = redis_cli.mget(cache_keys)

        ret_data, miss_keys = dict(), list()
        result = dict(izip(keys, cache_values))
        for key, value in result.iteritems():
            if value is not None:
                ret_data[key] = json.loads(value)
            else:
                miss_keys.append(key)

        return ret_data, miss_keys

    def redis_mset(redis_cli, key_prefix, miss_keys, reload_data):
        """pipeline mset"""
        pipe = redis_cli.pipeline()     # redis pipeline
        for key in miss_keys:
            str_key = str(key)
            if str_key not in reload_data:  # 未查到的键设置默认值
                reload_data[str_key] = default_value
            value = reload_data.get(str_key)
            pipe.set(key_prefix % str_key, json.dumps(value), redis_ttl)

        pipe.execute()

    def reload_missed_data(func, args, kwargs, miss_keys):
        """重载数据"""
        if not max_size:
            kwargs['keys'] = miss_keys
            return func(*args, **kwargs)

        # 查询数量有限制，分多次查询
        num = len(miss_keys)
        count = num / max_size \
            if (num % max_size == 0) \
            else (num / max_size + 1)

        all_data = dict()
        for i in range(count):
            start = i * max_size
            end = (i + 1) * max_size
            kwargs['keys'] = miss_keys[start: end]
            data = func(*args, **kwargs)
            all_data.update(data)
        return all_data

    @wrapt.decorator
    def wrapper(func, instance, args, kwargs):
        """
        :param instance:  instance is must
        :param args:      未限制
        :param kwargs:    必填keys, 选填redis_client, redis_key_prefix
        :return: data
        """
        ret_data = dict()
        redis_cli = redis_client or kwargs.get('redis_client')
        if not redis_cli:
            Log.error(
                'smart_batch, no redis connection! func: %s' % func.__name__)
            return ret_data

        key_prefix = redis_key_prefix or kwargs.get('redis_key_prefix')
        if not key_prefix:
            Log.error(
                'smart_batch, no redis key prefix! func: %s' % func.__name__)
            return ret_data
        if '%s' not in key_prefix:
            key_prefix += '%s'

        keys = kwargs.get('keys', [])
        if not keys:
            return ret_data
        keys = map(str, keys)

        ret_data, miss_keys = redis_mget(redis_cli, key_prefix, keys)
        if not miss_keys:
            return ret_data

        reload_data = reload_missed_data(func, args, kwargs, miss_keys)
        redis_mset(redis_cli, key_prefix, miss_keys, reload_data)

        ret_data.update(reload_data)
        return ret_data

    return wrapper


def smart_cached(ttl, redis_key=None, redis_client=None):
    """
    :author: gzzhangqiang2014@corp.netease.com
    :param redis_cli: redis connection
    :param redis_key: redis key
    :param ttl: expire time
    :return: data
    """
    @wrapt.decorator
    def wrapper(func, instance, args, kwargs):  # instance is must
        redis_cli = redis_client or kwargs.get('redis_client')
        if not redis_cli:
            Log.error(
                'Smart_cached, no redis connection! func: %s' % func.__name__)
            return None

        r_key = redis_key or kwargs.get('redis_key')
        if not r_key:
            Log.error(
                'Smart_cached, no redis key! func: %s' % func.__name__)
            return None

        data = redis_cli.get(r_key)
        Log.debug('Smart_cache, key: %s' % r_key)
        if data:
            return json.loads(data)
        else:
            data = func(*args, **kwargs)
            redis_cli.setex(r_key, ttl, json.dumps(data))
            return data

    return wrapper


class SmartMongo(object):
    def __init__(self, mongo_cli, table_name, logger):
        """
        :param mongo_cli: mongo连接
        :param table_name: mongo表名
        :param logger: 日志对象
        """
        self.table_name = table_name
        self.mongo_cli = mongo_cli
        self.logger = logger

    def check_mongo_connection(self):
        """检查mongo连接"""
        if self.mongo_cli:
            return True
        else:
            self.logger.error(
                '[SmartMongo]could not get mongo connection! '
                'table_name: %s' % self.table_name)
            return False

    def insert(self, data):
        """insert 封装"""
        if not self.check_mongo_connection():
            return

        self.mongo_cli[self.table_name].insert(data)

    def find_one(self, condition, fields=None):
        """find_one 封装"""
        if not self.check_mongo_connection():
            return {}

        mongo_cli = self.mongo_cli
        table_name = self.table_name
        if fields is None:
            result = mongo_cli[table_name].find_one(condition)
        else:
            result = mongo_cli[table_name].find_one(condition, fields)
        return result or {}

    def find_all(self):
        """find封装"""
        if not self.check_mongo_connection():
            return []

        result = self.mongo_cli[self.table_name].find()
        return list(result)

    def query(self, condition, fields=None):
        if not self.check_mongo_connection():
            return []

        mongo_cli = self.mongo_cli
        table_name = self.table_name
        if fields is None:
            result = mongo_cli[table_name].find(condition)
        else:
            result = mongo_cli[table_name].find(condition, fields)
        return list(result)

    def set(self, query, set_data, upsert=False):
        """find $set"""
        if not self.check_mongo_connection():
            return {}

        res = self.mongo_cli[self.table_name].update(
            query, {'$set': set_data}, upsert=upsert)
        return res


class ApiCode(object):
    OK = 'OK'


class HttpCode(object):
    HTTP_200 = 200
    HTTP_404 = 404


class TimeOut(object):
    NORMAL = 2
    SHORT = 1


def request_get(url, params, timeout):
    """通用cgi请求"""
    func_name = sys._getframe(1).f_code.co_name
    try:
        result = requests.get(url=url, params=params, timeout=timeout)
        code, text = result.status_code, result.text
    except Exception, e:
        Log.error('requests.get() exception! func_name: %s, '
                  'error: %s, url: %s, params: %s' %
                  (func_name, e, url, json.dumps(params)))
        return -1, {}

    if code != HttpCode.HTTP_200:
        Log.error('HttpCode_not_200! func_name: %s,'
                  ' code: %s, text: %s, url: %s, params: %s' %
                  (func_name, code, text, url, json.dumps(params)))
        return code, {}

    try:
        data = json.loads(text)
        return code, data
    except Exception, e:
        Log.error('json.loads() exception! func_name: %s, '
                  'error: %s, url: %s, params: %s' %
                  (func_name, e, url, json.dumps(params)))
        return -3, {}


def request_get_api(url, params, timeout):
    """请求微服务接口"""
    func_name = sys._getframe(1).f_code.co_name

    code, data = request_get(url, params, timeout)
    if code != HttpCode.HTTP_200:
        return code, data

    api_code = data.get('code')
    if api_code != ApiCode.OK:
        Log.error('ApiCode_not_OK! func_name: %s,'
                  'url: %s, params: %s, code: %s, response: %s' %
                  (func_name, url, params, api_code, data))
        return -4, {}
    else:
        api_data = data.get('data', {})
        return code, api_data


# vim: nu et ts=4 sw=4
