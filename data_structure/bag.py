#!/usr/bin/env python
# -*- coding:utf-8 -*-

"""
背包

public class Bag<Item> implements  Iterable<Item>
    Bag() 创建一个空背包
    void add(Item item) 添加一个元素
    boolean isEmpty() 背包是否为空
    int size() 背包中的元素数量
"""


class Bag(object):
    def __init__(self, items=None):
        self._items = []
        self._length = 0
        if items is None:
            return
        for i in items:
            self.add(i)

    def add(self, item):
        self._items.append(item)
        self._length += 1

    def isEmpty(self):
        return (self._length == 0)

    def size(self):
        return self._length

    def __repr__(self):
        return 'Bag(%r)' % self._items


if __name__ == "__main__":
    b = Bag([1,2,3,4])
    print(b.size())
    print(b.isEmpty())
    b.add(2)
    print(b)
