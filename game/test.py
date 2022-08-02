
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
        self.time = time

class MyCache:
    def __init__(self, size) -> None:
        self.size = size
        self.mapping: Dict[str, Item] = OrderedDict()

    def set(self, key, val):
        if key in self.mapping:
            item = self.mapping[key]
            item.val = val
            item.time = now()
            self.mapping.move_to_end(key)
        elif len(self.mapping) < self.size:
            self.mapping[key] = Item(val, now)
        else:
            self.mapping.popitem()
            self.mapping[key] = Item(val, now)

    def get(self, key):
        item = self.mapping.pop(key, None)
        if item:
            return item.val
        return


def cache(times, expire):
    _m = {}
    @functools.wraps
    def wrapper(func):
        def inner(*args, **kw):
            key = f'{func.__name__}'
            key_args = f'{args}{kw}'
            res = _m.setdefault(key, MyCache()).get(key_args)
            if res:
                return

def c():
    return "c"

def b():
    c()
    return "b"

def a():
    b()
    c()
    return "a"
