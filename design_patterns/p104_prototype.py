"""原型模式
核心是原型类必须实现clone接口, 能够简单地从自身复制出新对象.
使用者不用了解原型类的构造逻辑
还可以进一步实现一个注册中心, 将原型类统一管理起来
"""

import copy
from dataclasses import dataclass
from typing import Optional

class CloneMixin:
    def clone(self, **attr):
        obj = copy.deepcopy(self)
        obj.__dict__.update(attr)
        return obj

class Prototype:
    def __init__(self):
        self.objects = dict()

    def register(self, identifier: str, obj: CloneMixin):
        self.objects[identifier] = obj

    def unregister(self, identifier):
        del self.objects[identifier]

    def get_proto(self, identifier: str, default=None) -> Optional[CloneMixin]:
        return self.objects.get(identifier, default)

@dataclass
class Software(CloneMixin):
    repo: str
    version: str
    language: str
    date: str

@dataclass
class Book(CloneMixin):
    name: str
    author: str
    version: str
    date: str

def main():
    proto = Prototype()
    proto.register('gcc', Software('gcc', '0.1', 'c++', '1978'))
    proto.register('csapp', Book('csapp', 'MIT', 'first edition', '2000'))
    gcc5 = proto.get_proto('gcc').clone(version='5.0', date='2018')
    print(gcc5)
    csapp3 = proto.get_proto('csapp').clone(version='third edition', date='2020')
    print(csapp3)

if __name__ == '__main__':
    main()
