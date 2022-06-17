"""装饰器

当你想给原有代码增加额外的功能, 装饰器可以多层嵌套
"""

import time
import functools

class Database:
    def __init__(self, idx: int=0) -> None:
        self.idx = idx

    def ping(self):
        pass

class MySQL(Database):
    def ping(self):
        time.sleep(0.1)
        return f'<MySQL idx={self.idx}>'


class Timer(Database):
    def __init__(self, db: MySQL) -> None:
        self.db = db

    def ping(self):
        start = time.time()
        res = self.db.ping()
        print(f'call {self.db} cost: {time.time()-start:.4f}')
        return res


def timer_decorator(func):
    @functools.wraps(func)
    def wrapper(*args, **kw):
        start = time.time()
        res = func(*args, **kw)
        print(f'call {func} cost: {time.time()-start:.4f}')
        return res
    return wrapper

def main():
    db = MySQL(11)
    print(db.ping())
    timer = Timer(db)
    print(timer.ping())

    # 函数风格装饰器
    print(timer_decorator(db.ping)())

if __name__ == '__main__':
    main()
