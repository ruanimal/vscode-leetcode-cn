#!/usr/bin/env python
# -*- coding:utf-8 -*-


class Stack(object):
    def __init__(self, items=None):
        self._items = []
        self._length = 0

        if items is None:
            return
        for i in items:
            self.push(i)

    def push(self, item):
        self._items.append(item)
        self._length += 1

    def pop(self):
        val = self._items.pop()
        self._length -= 1
        return val

    def isEmpty(self):
        return (self._length == 0)

    def size(self):
        return self._length

    def __repr__(self):
        return 'Stack(%r)' % self._items


if __name__ == "__main__":
    b = Stack([1, 2, 3, 4])
    print(b.size())
    print(b.isEmpty())
    b.push(2)
    print(b)
    b.pop()
    print(b)
