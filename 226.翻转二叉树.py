#
# @lc app=leetcode.cn id=226 lang=python
#
# [226] 翻转二叉树
#
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def invertTree(self, root):
        """
        :type root: TreeNode
        :rtype: TreeNode
        """
        if not root:
            return
        # tmp = root.left
        # root.left = self.invertTree(root.right)
        # root.right = self.invertTree(tmp)
        root.left, root.right = self.invertTree(root.right), self.invertTree(root.left)
        return root

