#
# @lc app=leetcode.cn id=111 lang=python3
#
# [111] 二叉树的最小深度
#
# https://leetcode-cn.com/problems/minimum-depth-of-binary-tree/description/
#
# algorithms
# Easy (36.82%)
# Total Accepted:    14.4K
# Total Submissions: 37.9K
# Testcase Example:  '[3,9,20,null,null,15,7]'
#
# 给定一个二叉树，找出其最小深度。
#
# 最小深度是从根节点到最近叶子节点的最短路径上的节点数量。
#
# 说明: 叶子节点是指没有子节点的节点。
#
# 示例:
#
# 给定二叉树 [3,9,20,null,null,15,7],
#
# ⁠   3
# ⁠  / \
# ⁠ 9  20
# ⁠   /  \
# ⁠  15   7
#
# 返回它的最小深度  2.
#
#

from comm import *
# @lc code=start
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None


class SolutionA(object):
    def minDepth(self, root: TreeNode) -> int:
        """
        简单递归, 在后序位置, 要遍历完整颗树, 比较慢
        """
        if (root == None):
            return 0
        if (root.left == None and root.right == None):
            return 1
        if (root.left == None):
            return 1 + self.minDepth(root.right)
        if (root.right == None):
            return 1 + self.minDepth(root.left)
        return 1 + min(self.minDepth(root.left), self.minDepth(root.right))

class Solution(object):
    def minDepth(self, root: TreeNode) -> int:
        """
        层次遍历, 有一个节点左右子节点都空, 则跳出
        """
        if (root == None):
            return 0

        level = [root]
        deep = 1
        while level:
            new_level = []
            for i in level:
                if not i.left and not i.right:
                    new_level = []
                    break
                if i.left:
                    new_level.append(i.left)
                if i.right:
                    new_level.append(i.right)
            level = new_level
            deep += 1
        if len(level) == 2 ** (deep-1):
            return deep
        return deep-1

# @lc code=end

