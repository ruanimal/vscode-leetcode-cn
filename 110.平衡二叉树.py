#
# @lc app=leetcode.cn id=110 lang=python3
#
# [110] 平衡二叉树
#
# https://leetcode.cn/problems/balanced-binary-tree/description/
#
# algorithms
# Easy (59.24%)
# Likes:    1590
# Dislikes: 0
# Total Accepted:    699.9K
# Total Submissions: 1.2M
# Testcase Example:  '[3,9,20,null,null,15,7]'
#
# 给定一个二叉树，判断它是否是 平衡二叉树  
#
#
#
# 示例 1：
#
#
# 输入：root = [3,9,20,null,null,15,7]
# 输出：true
#
#
# 示例 2：
#
#
# 输入：root = [1,2,2,3,3,null,null,4,4]
# 输出：false
#
#
# 示例 3：
#
#
# 输入：root = []
# 输出：true
#
#
#
#
# 提示：
#
#
# 树中的节点数在范围 [0, 5000] 内
# -10^4 <= Node.val <= 10^4
#
#
#

from comm import *

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

"""
一棵二叉树是平衡二叉树(不要求是搜索树)，如果对于每个节点，
其左子树和右子树的高度差不超过 1
每个子树也必须是平衡二叉树。
"""

T: TypeAlias = Optional[TreeNode]

class SolutionV0:
    def isBalanced(self, root: T) -> bool:
        if not root:
            return True
        delta = self.get_depth(root.left) - self.get_depth(root.right)
        return abs(delta) <= 1 and self.isBalanced(root.left) and self.isBalanced(root.right)

    def get_depth(self, root: T) -> int:
        if not root:
            return 0
        return max(self.get_depth(root.right), self.get_depth(root.left)) + 1


class Solution:
    def isBalanced(self, root: T) -> bool:
        return self.get_depth(root) >= 0

    def get_depth(self, root: T) -> int:
        """求平衡的树深度"""

        if not root:
            return 0
        l = self.get_depth(root.left)
        r = self.get_depth(root.right)
        if l == -1 or r == -1 or abs(l-r)>1:
            return -1
        return max(l, r) + 1

# @lc code=end

