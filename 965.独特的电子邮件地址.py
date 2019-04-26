#
# @lc app=leetcode.cn id=965 lang=python
#
# [965] 独特的电子邮件地址
#
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def isUnivalTree(self, root, pre=None):
        """
        :type root: TreeNode
        :rtype: bool
        """
        if not root:
            return True
        if pre is not None and pre != root.val:
            # print(repr(pre), repr(root.val))
            return False
        pre = root.val
        left_is = self.isUnivalTree(root.left, pre)
        right_is = self.isUnivalTree(root.right, pre)
        return left_is and right_is


