#
# @lc app=leetcode.cn id=112 lang=python3
#
# [112] 路径总和
#
# https://leetcode-cn.com/problems/path-sum/description/
#
# algorithms
# Easy (45.27%)
# Likes:    140
# Dislikes: 0
# Total Accepted:    18.7K
# Total Submissions: 40.2K
# Testcase Example:  '[5,4,8,11,null,13,4,7,2,null,null,null,1]\n22'
#
# 给定一个二叉树和一个目标和，判断该树中是否存在根节点到叶子节点的路径，这条路径上所有节点值相加等于目标和。
#
# 说明: 叶子节点是指没有子节点的节点。
#
# 示例: 
# 给定如下二叉树，以及目标和 sum = 22，
#
# ⁠             5
# ⁠            / \
# ⁠           4   8
# ⁠          /   / \
# ⁠         11  13  4
# ⁠        /  \      \
# ⁠       7    2      1
#
#
# 返回 true, 因为存在目标和为 22 的根节点到叶子节点的路径 5->4->11->2。
#
#
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

from comm import *
# @lc code=start

class Solution:
    def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:
        """
        后序位置判断
        """
        if root is None:
            return False
        if root.left is None and root.right is None:
            return True if targetSum == root.val else False
        elif root.left and root.right:
            return self.hasPathSum(root.left, targetSum-root.val) \
                or self.hasPathSum(root.right, targetSum-root.val)
        elif root.left:
            return self.hasPathSum(root.left, targetSum-root.val)
        else:
            return self.hasPathSum(root.right, targetSum-root.val)
# @lc code=end


