
'''
采用一个或多个装饰器实现如下功能，可采用类管理方式

1. 缓存函数最近(N)次的输入和输出，可控制每个缓存存在的时间为(M)秒，命中缓存则直接返回结果

2. 函数根据设定的期待输出(X)至多进行(N)次重试

3. 打印函数调用链，比如有如下函数a、b、c，执行a()，打印a->b->c，a->c（打印形式可变，表达清楚即可）

'''

import time
import functools
from collections import deque
from collections import OrderedDict
from typing import Dict

def now():
    return int(time.time())

class Item:
    def __init__(self, val, time) -> None:
        self.val = val
        self.time: int = time

    def __repr__(self):
        return '<{!r}, ttl: {}>'.format(self.val, self.time)

class MyCache:
    def __init__(self, size, expire) -> None:
        self.size: int = size
        self.expire: int = expire
        self.mapping: Dict[str, Item] = OrderedDict()

    def set(self, key, val):
        if key in self.mapping:
            item = self.mapping[key]
            item.val = val
            item.time = now()
            self.mapping.move_to_end(key)
        elif len(self.mapping) < self.size:
            self.mapping[key] = Item(val, now())
        else:
            self.mapping.popitem(last=False)
            self.mapping[key] = Item(val, now())

    def get(self, key):
        item = self.mapping.get(key)
        if item is None:
            return
        if (now() - item.time) > self.expire:
            self.mapping.pop(key)
            return
        return item.val

    def __repr__(self) -> str:
        return f'<size: {self.size}, {dict(self.mapping)}>'

def cache(times, expire):
    _m = {}
    def wrapper(func):
        @functools.wraps(func)
        def inner(*args, **kw):
            key = f'{func.__name__}'
            key_args = f'{args}{kw}'
            res = _m.setdefault(key, MyCache(times, expire)).get(key_args)
            if res is None:
                print('calling', key, key_args)
                res = func(*args, **kw)
                _m[key].set(key_args, res)
            print('==', _m)
            return res
        return inner
    return wrapper

def with_retry(times: int, expect):
    def wrapper(func):
        @functools.wraps(func)
        def inner(*args, **kw):
            res = None
            for i in range(times):
                res = func(*args, **kw)
                print(f'{i}th call, res: {res}')
                if res == expect:
                    return res
            return res
        return inner
    return wrapper


def traceing(main=False):
    def wrapper(func):
        @functools.wraps(func)
        def inner(*args, **kw):
            print(f'{func.__name__} ->', end=' ')
            res = func(*args, **kw)
            return res
        return inner
    return wrapper

@cache(2, 1)
def c(x=1):
    return f"c-{x}"

@traceing()
def c1():
    return 'c1'

@traceing()
def b1():
    c1()
    return "b"

@traceing(main=True)
def a1():
    b1()
    c1()
    return "a"

@with_retry(3, 1)
def d():
    import random
    return random.randrange(1, 5)

def test_cache():
    print(c())
    print(c())
    time.sleep(2)
    print(c())
    print(c(2))
    print(c(3))
    print(c())

def test_with_retry():
    d()
    d()
    d()

def test_traceing():
    a1()

if __name__ == '__main__':
    # import ipdb;ipdb.set_trace()
    test_traceing()
