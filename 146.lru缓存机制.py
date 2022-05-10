#
# @lc app=leetcode.cn id=146 lang=python3
#
# [146] LRU缓存机制
#
# https://leetcode-cn.com/problems/lru-cache/description/
#
# algorithms
# Hard (40.19%)
# Likes:    165
# Dislikes: 0
# Total Accepted:    9.7K
# Total Submissions: 23.3K
# Testcase Example:  '["LRUCache","put","put","get","put","get","put","get","get","get"]\n[[2],[1,1],[2,2],[1],[3,3],[2],[4,4],[1],[3],[4]]'
#
# 运用你所掌握的数据结构，设计和实现一个  LRU (最近最少使用) 缓存机制。它应该支持以下操作： 获取数据 get 和 写入数据 put 。
#
# 获取数据 get(key) - 如果密钥 (key) 存在于缓存中，则获取密钥的值（总是正数），否则返回 -1。
# 写入数据 put(key, value) -
# 如果密钥不存在，则写入其数据值。当缓存容量达到上限时，它应该在写入新数据之前删除最近最少使用的数据值，从而为新的数据值留出空间。
#
# 进阶:
#
# 你是否可以在 O(1) 时间复杂度内完成这两种操作？
#
# 示例:
#
# LRUCache cache = new LRUCache( 2 /* 缓存容量 */ );
#
# cache.put(1, 1);
# cache.put(2, 2);
# cache.get(1);       // 返回  1
# cache.put(3, 3);    // 该操作会使得密钥 2 作废
# cache.get(2);       // 返回 -1 (未找到)
# cache.put(4, 4);    // 该操作会使得密钥 1 作废
# cache.get(1);       // 返回 -1 (未找到)
# cache.get(3);       // 返回  3
# cache.get(4);       // 返回  4
#
#
#

# @lc code=start

from collections import OrderedDict

class LRUCacheV1(OrderedDict):
    """利用库函数实现"""

    def __init__(self, capacity: int):
        OrderedDict.__init__(self)
        self._capacity = capacity

    def get(self, key: int) -> int:
        if key not in self:
            return -1
        val = self.pop(key)
        self[key] = val
        return val

    def put(self, key: int, value: int):
        if key in self:
            self.pop(key)
        self[key] = value
        if len(self) > self._capacity:
            self.popitem(last=False)


class Node:
    def __init__(self, key, val=None):
        self.key = key
        self.val = val
        self.next = None
        self.prev = None

    def __repr__(self):
        return 'Node({!r}, {!r})'.format(self.key, self.val)


class DoublyLink:
    def __init__(self):
        self.root = Node('root')
        self.root.prev = self.root
        self.root.next = self.root
        self.length = 0

    @property
    def tail(self) -> Node:
        return self.root.prev

    def append_head(self, node):
        return self.insert_after(self.root, node)

    def append_tail(self, node):
        return self.insert_after(self.tail, node)

    def insert_after(self, pos: Node, node):
        pos.next.prev = node
        node.next = pos.next
        pos.next = node
        node.prev = pos
        self.length += 1
        return node

    def find(self, key):
        ptr = self.root
        while ptr.next != self.root:
            if ptr.next.key == key:
                return ptr.next
            ptr = ptr.next

    def remove(self, node):
        if node == self.root:
            return False
        node.next.prev = node.prev
        node.prev.next = node.next
        self.length -= 1
        del node
        return True

    def __repr__(self):
        tmp = ['Link(len={}):'.format(self.length)]
        ptr = self.root
        while ptr.next != self.root:
            tmp.append(repr(ptr.next))
            ptr = ptr.next
        return ' -> '.join(tmp)


class LRUCache:
    def __init__(self, capacity):
        self.cache = {}
        self.dl = DoublyLink()
        self.size = capacity

    def check_expired(self):
        if self.dl.length == self.size:
            self.cache.pop(self.dl.tail.key)
            self.dl.remove(self.dl.tail)

    def move_to_head(self, node):
        self.dl.remove(node)
        self.dl.append_head(node)

    def get(self, key):
        node = self.cache.get(key, None)
        if not node:
            return -1
        self.move_to_head(node)
        return node.val

    def put(self, key, val):
        node = self.cache.get(key, None)
        if node:
            node.val = val
            self.move_to_head(node)
            return
        self.check_expired()
        self.cache[key] = self.dl.append_head(Node(key, val))

    def __repr__(self):
        return '<LRU maxsize={}, len={}> {!r}'.format(self.size, self.dl.length, self.cache)


# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)

# @lc code=end

if __name__ == "__main__":
    cmds = [
        ["put","put","get","put","get","put","get","get","get"],
        [[1,1],[2,2],[1],[3,3],[2],[4,4],[1],[3],[4]]
    ]
    cache = LRUCache(2)
    for m, args in zip(*cmds):
        func = getattr(cache, m)
        print(func(*args))
        # print(cache)
