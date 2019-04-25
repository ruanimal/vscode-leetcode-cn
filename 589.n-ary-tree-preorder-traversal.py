#
# @lc app=leetcode.cn id=589 lang=python
#
# [589] N-ary Tree Preorder Traversal
#
"""
# Definition for a Node.
class Node(object):
    def __init__(self, val, children):
        self.val = val
        self.children = children
"""
class Solution(object):
    def preorder(self, root, ret=None):
        """
        :type root: Node
        :rtype: List[int]
        """
        # # 递归版本
        # if ret is None:
        #     ret = []
        # if not root:
        #     return
        # ret.append(root.val)
        # for i in root.children:
        #     self.preorder(i, ret)
        # return ret

        # 迭代版本
        if not root:
            return
        ret = []
        stack = [root]
        while stack:
            top = stack.pop()
            ret.append(top.val)
            for i in top.children[::-1]:
                stack.append(i)
        return ret


