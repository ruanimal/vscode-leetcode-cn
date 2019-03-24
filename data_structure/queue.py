#!/usr/bin/env python
# -*- coding:utf-8 -*-

from list_node import ListNode  #

class Queue(object):
    def __init__(self, items=None):
        self._items = ListNode(None)
        self._length = 0
        self._end_ptr = self._items
        if items is None:
            return
        for i in items:
            self.enqueue(i)

    def enqueue(self, item):
        self._end_ptr.next = ListNode(item)
        self._end_ptr = self._end_ptr.next
        self._length += 1

    def dequeue(self):
        assert self._items
        tmp = self._items.next
        self._items = self._items.next
        self._length -= 1
        return tmp.val

    def isEmpty(self):
        return (self._length == 0)

    def size(self):
        return self._length

    def __repr__(self):
        return '%s(%r)' % (self.__class__.__name__, self._items.next)


if __name__ == "__main__":
    b = Queue([1, 2, 3, 4])
    print(b.isEmpty())
    b.enqueue(2)
    print(b)
    print(b.size())
    while not b.isEmpty():
        b.dequeue()
        print(b)
