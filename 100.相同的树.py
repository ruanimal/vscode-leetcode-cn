#
# @lc app=leetcode.cn id=100 lang=python
#
# [100] 相同的树
#
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def isSameTree(self, p, q):
        """
        :type p: TreeNode
        :type q: TreeNode
        :rtype: bool
        """
        if not p and not q:
            return True
        elif p and q:
            if p.val == q.val:
                if self.isSameTree(p.left, q.left) and self.isSameTree(p.right, q.right):
                    return True
        return False

