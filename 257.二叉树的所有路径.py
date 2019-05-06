#
# @lc app=leetcode.cn id=257 lang=python
#
# [257] 二叉树的所有路径
#
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def binaryTreePaths(self, root):
        """
        :type root: TreeNode
        :rtype: List[str]
        """
        ans = []
        def dfs(node, path=None):
            if path is None:
                path = []
            path.append(str(node.val))
            if not node.left and not node.right:
                ans.append('->'.join(path))
                return
            if node.left:
                dfs(node.left, path)
                path.pop()
            if node.right:
                dfs(node.right, path)
                path.pop()

        if not root:
            return
        dfs(root)
        return ans

