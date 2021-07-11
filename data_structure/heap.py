"""
二叉堆
"""

from math import log, ceil

class Heap(object):
    def __init__(self):
        self._items = [None]
        self.need_swap = self.less

    @property
    def length(self):
        return len(self._items) - 1

    @property
    def depth(self):
        return ceil(log(self.length+1, 2))

    def less(self, i, j):
        return self._items[i] < self._items[j]

    def more(self, i, j):
        return self._items[i] > self._items[j]

    def exch(self, i, j):
        self._items[i], self._items[j] = self._items[j], self._items[i]

    def swim(self, k):
        while k > 1 and self.need_swap(k//2, k):
            self.exch(k//2, k)
            k = k//2

    def sink(self, k):
        while 2 * k <= self.length:
            j = 2 * k
            if j < self.length and self.need_swap(j, j+1):
                j += 1
            if not self.need_swap(k, j):
                break
            self.exch(k, j)
            k = j

    def insert(self, val):
        self._items.append(val)
        self.swim(self.length)

    def top(self):
        if self.length > 0:
            return self._items[1]

    def del_top(self):
        if self.length > 0:
            self.exch(1, self.length)
            val = self._items.pop()
            self.sink(1)
            return val

    def __repr__(self):
        tmp = []
        seq = ' '
        for i in range(1, self.depth+1):
            l = seq.join([str(e) for e in self._items[2**(i-1):2**i]])
            tmp.append(l)
        return '\n'.join(tmp)


class MinHeap(Heap):
    def __init__(self):
        super(MinHeap, self).__init__()
        self.need_swap = self.more

if __name__ == "__main__":
    import random
    nums = list(range(8))
    random.shuffle(nums)
    print(nums)
    obj = MinHeap()
    for i in nums:
        obj.insert(i)
        print('min', obj.top(), obj._items)
    print(obj)
    while obj.length > 0:
        print(obj.del_top(), obj._items)
    print('++' * 20)
    nums = list(range(8))
    random.shuffle(nums)
    print(nums)
    obj = Heap()
    for i in nums:
        obj.insert(i)
        print('max', obj.top(), obj._items)
    print(obj)
    while obj.length > 0:
        print(obj.del_top(), obj._items)


