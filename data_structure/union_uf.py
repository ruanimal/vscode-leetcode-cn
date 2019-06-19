#!/usr/bin/env python
# -*- coding:utf-8 -*-


class QuickUnionUF:
    def __init__(self, n):
        self.roots = [i for i in range(n)]

    def findRoot(self, i):
        root = i
        while root != self.roots[root]:
            root = self.roots[root]
        while i != self.roots[i]:
            tmp = self.roots[i]
            self.roots[i] = root
            i = tmp
        return root

    def connected(self, p, q):
        return self.findRoot(p) == self.findRoot(q)

    def union(self, p, q):
        pr = self.findRoot(p)
        qr = self.findRoot(q)
        self.roots[pr] = qr
