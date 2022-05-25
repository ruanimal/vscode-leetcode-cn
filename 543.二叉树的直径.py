#
# @lc app=leetcode.cn id=543 lang=python3
#
# [543] 二叉树的直径
#
# https://leetcode-cn.com/problems/diameter-of-binary-tree/description/
#
# algorithms
# Easy (45.12%)
# Likes:    100
# Dislikes: 0
# Total Accepted:    6K
# Total Submissions: 13.3K
# Testcase Example:  '[1,2,3,4,5]'
#
# 给定一棵二叉树，你需要计算它的直径长度。一棵二叉树的直径长度是任意两个结点路径长度中的最大值。这条路径可能穿过根结点。
#
# 示例 :
# 给定二叉树
#
#
# ⁠         1
# ⁠        / \
# ⁠       2   3
# ⁠      / \
# ⁠     4   5
#
#
# 返回 3, 它的长度是路径 [4,2,1,3] 或者 [5,2,1,3]。
#
# 注意：两结点之间的路径长度是以它们之间边的数目表示。
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

class Solution:
    def diameterOfBinaryTree(self, root: TreeNode) -> int:
        """当前直径为子树直径的较大者, 再加一
        """
        if not root:
            return 0
        self.ans = 0
        self.find_width(root)
        return self.ans

    def find_width(self, node):
        """
        注意理解递归返回的是什么, 有多少种情况
        遍历过程中,在什么时候更新了什么状态
        """

        if not node and not node:
            return 0

        left_depth = self.find_width(node.left)   # 左子树直径
        right_depth = self.find_width(node.right)
        self.ans = max(self.ans, left_depth + right_depth)
        return max(left_depth, right_depth) + 1   # 当前直径为子树直径的较大者, 再加一

# @lc code=end


