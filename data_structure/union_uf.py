#!/usr/bin/env python
# -*- coding:utf-8 -*-


class UnionFind:
    def __init__(self, n):
        self.parent = [i for i in range(n)]  # parent[i] = j 表示i节点的根节点是j
        self.count = n

    def find(self, p):
        if self.parent[p] != p:   # 不是根节点
            self.parent[p] = self.find(self.parent[p])   # 路径折叠
        return self.parent[p]

    def connected(self, p, q):
        return self.find(p) == self.find(q)

    def union(self, p, q):
        pr = self.find(p)
        qr = self.find(q)
        if pr == qr:    # 本来就在同一个连通分量中
            return
        self.parent[pr] = qr
        self.count -= 1


uf = UnionFind(10)
uf.union(1,2)
print(uf.parent)
uf.union(1,7)
print(uf.parent)
