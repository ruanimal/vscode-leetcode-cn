#
# @lc app=leetcode.cn id=590 lang=python
#
# [590] N-ary Tree Postorder Traversal
#
"""
# Definition for a Node.
class Node(object):
    def __init__(self, val, children):
        self.val = val
        self.children = children
"""
class Solution(object):
    def postorder(self, root, ret=None):
        """
        :type root: Node
        :rtype: List[int]
        """
        # 递归版本
        if ret is None:
            ret = []
        if not root:
            return
        for i in root.children:
            self.postorder(i, ret)
        ret.append(root.val)
        return ret
        # todo: 迭代版本
