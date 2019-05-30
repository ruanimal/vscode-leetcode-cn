#
# @lc app=leetcode.cn id=653 lang=python
#
# [653] 两数之和 IV - 输入 BST
#
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def findTarget(self, root, k):
        """
        :type root: TreeNode
        :type k: int
        :rtype: bool
        """
        def dfs(root):
            if not root:
                return
            nodes_map[root.val] = id(root)
            dfs(root.left)
            dfs(root.right)

        nodes_map = {}
        dfs(root)
        for key, val in nodes_map.items():
            # 防止某个节点被使用两次
            if (k - key) in nodes_map and nodes_map[k - key] != val:
                return True
        return False


