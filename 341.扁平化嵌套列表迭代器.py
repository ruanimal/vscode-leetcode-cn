#
# @lc app=leetcode.cn id=341 lang=python3
#
# [341] 扁平化嵌套列表迭代器
#
# https://leetcode-cn.com/problems/flatten-nested-list-iterator/description/
#
# algorithms
# Medium (72.54%)
# Likes:    420
# Dislikes: 0
# Total Accepted:    57.8K
# Total Submissions: 79.7K
# Testcase Example:  '[[1,1],2,[1,1]]'
#
# 给你一个嵌套的整数列表 nestedList
# 。每个元素要么是一个整数，要么是一个列表；该列表的元素也可能是整数或者是其他列表。请你实现一个迭代器将其扁平化，使之能够遍历这个列表中的所有整数。
#
# 实现扁平迭代器类 NestedIterator ：
#
#
# NestedIterator(List<NestedInteger> nestedList) 用嵌套列表 nestedList 初始化迭代器。
# int next() 返回嵌套列表的下一个整数。
# boolean hasNext() 如果仍然存在待迭代的整数，返回 true ；否则，返回 false 。
#
#
# 你的代码将会用下述伪代码检测：
#
#
# initialize iterator with nestedList
# res = []
# while iterator.hasNext()
# ⁠   append iterator.next() to the end of res
# return res
#
# 如果 res 与预期的扁平化列表匹配，那么你的代码将会被判为正确。
#
#
#
# 示例 1：
#
#
# 输入：nestedList = [[1,1],2,[1,1]]
# 输出：[1,1,2,1,1]
# 解释：通过重复调用 next 直到 hasNext 返回 false，next 返回的元素的顺序应该是: [1,1,2,1,1]。
#
# 示例 2：
#
#
# 输入：nestedList = [1,[4,[6]]]
# 输出：[1,4,6]
# 解释：通过重复调用 next 直到 hasNext 返回 false，next 返回的元素的顺序应该是: [1,4,6]。
#
#
#
#
# 提示：
#
#
# 1 <= nestedList.length <= 500
# 嵌套列表中的整数值在范围 [-10^6, 10^6] 内
#
#
#

# @lc code=start
# """
# This is the interface that allows for creating nested lists.
# You should not implement it, or speculate about its implementation
# """

from typing import *

class NestedInteger:
   def isInteger(self) -> bool:
       """
       @return True if this NestedInteger holds a single integer, rather than a nested list.
       """

   def getInteger(self) -> int:
       """
       @return the single integer that this NestedInteger holds, if it holds a single integer
       Return None if this NestedInteger holds a nested list
       """

   def getList(self) -> List['NestedInteger']:
       """
       @return the nested list that this NestedInteger holds, if it holds a nested list
       Return None if this NestedInteger holds a single integer
       """

class NestedIterator_A:
    def __init__(self, nestedList: List[NestedInteger]):
        """
        直接展开法
        """

        self.res = []
        self.index = -1
        for i in nestedList:
            self.helper(i)

    def helper(self, data: NestedInteger):
        if data.isInteger():
            self.res.append(data.getInteger())
            return
        for i in data.getList():
            self.helper(i)

    def next(self) -> int:
        if self.index == len(self.res)-1:
            return
        self.index += 1
        return self.res[self.index]

    def hasNext(self) -> bool:
        return self.index < len(self.res)-1

class NestedIterator_B:
    def __init__(self, nestedList: List[NestedInteger]):
        """
        原生生成器版本
        """
        self.finish = False
        self.current = None
        self.gen = self.helper(nestedList)

    def helper(self, data: List[NestedInteger]):
        for i in data:
            if i.isInteger():
                yield i.getInteger()
            else:
                yield from self.helper(i.getList())

    def next(self) -> int:
        return self.current

    def hasNext(self) -> bool:
        try:
            self.current = next(self.gen)
            return True
        except StopIteration:
            self.current = None
            return False

from collections import deque

class NestedIterator_C:
    def __init__(self, nestedList: List[NestedInteger]):
        """
        双端队列版本
        """
        self.que = deque()
        self.que.extend(nestedList)

    def next(self) -> int:
        return self.que.popleft().getInteger()

    def hasNext(self) -> bool:
        while self.que and not self.que[0].isInteger():
            tmp = self.que.popleft().getList()
            for i in range(len(tmp)-1, -1, -1):
                self.que.appendleft(tmp[i])
        return len(self.que) > 0

class NestedIterator:
    def __init__(self, nestedList: List[NestedInteger]):
        """
        list 版本
        """
        self.que = []
        self.que.extend(nestedList[::-1])

    def next(self) -> int:
        return self.que.pop().getInteger()

    def hasNext(self) -> bool:
        while self.que and not self.que[-1].isInteger():
            self.que.extend(self.que.pop().getList()[::-1])
        return len(self.que) > 0

# Your NestedIterator object will be instantiated and called as such:
# i, v = NestedIterator(nestedList), []
# while i.hasNext(): v.append(i.next())
# @lc code=end

