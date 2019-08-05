# -*- coding:utf-8 -*-

"""
优先队列
"""

class MaxPQ(object):
    def __init__(self, items=None):
        self._items = []
        self._length = 0

        if items is None:
            return
        for i in items:
            self.Insert(i)

    def Insert(self, v):
        for i in range(self._length):
            if v < self._items[i]:
                self._items.insert(i, v)
                break
        else:
            self._items.append(v)
        self._length += 1

    def max(self):
        if self._length <= 0:
            return
        return self._items[self._length -1]

    def delMax(self):
        if self._length <= 0:
            return
        val = self._items.pop()
        self._length -= 1
        return val

    def isEmpty(self):
        return (self._length == 0)

    def size(self):
        return self._length

    def __repr__(self):
        return '%s(%r)' % (self.__class__.__name__, self._items)

if __name__ == "__main__":
    obj = MaxPQ(range(10))
    print(obj.size())
    print(obj.isEmpty())
    obj.Insert(99)
    print(obj.delMax())
    print(obj.max())
    print(obj)
