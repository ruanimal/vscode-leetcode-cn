#
# @lc app=leetcode.cn id=637 lang=python
#
# [637] 二叉树的层平均值
#
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def averageOfLevels(self, root):
        """
        :type root: TreeNode
        :rtype: List[float]
        """
        ans = []
        level = [root]
        while level:
            next_level = []
            tmp = 0.0
            for i in level:
                tmp += i.val
                if i.left:
                    next_level.append(i.left)
                if i.right:
                    next_level.append(i.right)
            ans.append(tmp/len(level))
            level = next_level
        return ans


