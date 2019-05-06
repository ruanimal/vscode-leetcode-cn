#
# @lc app=leetcode.cn id=872 lang=python
#
# [872] 叶子相似的树
#
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def leafSimilar(self, root1, root2):
        """
        :type root1: TreeNode
        :type root2: TreeNode
        :rtype: bool
        """
        def find_leaf(node, leafs=None):
            if leafs is None:
                leafs = []
            if not node.left and not node.right:
                leafs.append(node.val)
                return leafs
            if node.left:
                find_leaf(node.left, leafs)
            if node.right:
                find_leaf(node.right, leafs)
            return leafs
        return find_leaf(root1) == find_leaf(root2)

