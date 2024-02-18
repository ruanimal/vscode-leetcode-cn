# encoding: utf-8
# a = input("please input a number:")
# print("hello world")

import heapq
from dataclasses import dataclass, field
from typing import Any


@dataclass(order=True)
class Item:
    priority: int
    item: Any = field(compare=False)

    def __str__(self):
        return str((self.priority, self.item))


def find_freq(words: list, kth: int):
    counter = {}
    for i in words:
        counter[i] = counter.get(i, 0) + 1

    if kth > len(counter):
        raise ValueError

    heap = []
    for k, v in counter.items():
        item = Item(v, k)
        if len(heap) < kth:
            heapq.heappush(heap, item)
        else:
            heapq.heapreplace(heap, item)
    return heap[0]

words = ['a', 'a', 'b', 'c', 'c', 'c']
res = find_freq(words, 3)
print(res)
