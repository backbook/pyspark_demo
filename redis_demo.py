# -*- coding:utf-8 -*-

import redis


r = redis.Redis(host='127.0.0.1', port=6379, decode_responses=True)
r.set('foo', 'Bar')
print(r.get('foo'))
