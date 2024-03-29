#
# @lc app=leetcode.cn id=106 lang=python3
#
# [106] 从中序与后序遍历序列构造二叉树
#
# https://leetcode-cn.com/problems/construct-binary-tree-from-inorder-and-postorder-traversal/description/
#
# algorithms
# Medium (72.29%)
# Likes:    691
# Dislikes: 0
# Total Accepted:    171.2K
# Total Submissions: 236.8K
# Testcase Example:  '[9,3,15,20,7]\n[9,15,7,20,3]'
#
# 给定两个整数数组 inorder 和 postorder ，其中 inorder 是二叉树的中序遍历， postorder
# 是同一棵树的后序遍历，请你构造并返回这颗 二叉树 。
#
#
#
# 示例 1:
#
#
# 输入：inorder = [9,3,15,20,7], postorder = [9,15,7,20,3]
# 输出：[3,9,20,null,null,15,7]
#
#
# 示例 2:
#
#
# 输入：inorder = [-1], postorder = [-1]
# 输出：[-1]
#
#
#
#
# 提示:
#
#
# 1 <= inorder.length <= 3000
# postorder.length == inorder.length
# -3000 <= inorder[i], postorder[i] <= 3000
# inorder 和 postorder 都由 不同 的值组成
# postorder 中每一个值都在 inorder 中
# inorder 保证是树的中序遍历
# postorder 保证是树的后序遍历
#
#
#

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right


from comm import *
# @lc code=start

class Solution:
    def buildTree(self, inorder: List[int], postorder: List[int]) -> TreeNode:
        """
        参考 [105] 从前序与中序遍历序列构造二叉树, 只是需要调换左右子树构造顺序, 因为提供的是后序数组
        """

        if len(inorder) == 0 or len(postorder) == 0:
            return

        self.call_index = len(postorder)
        self.inorder_index = {i[1]:i[0] for i in enumerate(inorder)}
        return self.helper(inorder, postorder, 0, len(inorder)-1)

    def helper(self, inorder: List[int], postorder: List[int], left, right) -> TreeNode:
        if (right-left) < 0:
            return

        self.call_index -= 1
        idx = self.inorder_index[postorder[self.call_index]]
        root = TreeNode(inorder[idx])
        root.right = self.helper(inorder, postorder, idx+1, right)
        root.left = self.helper(inorder, postorder, left, idx-1)
        return root

# @lc code=end

s = Solution()
print(s.buildTree([9,3,15,20,7], [9,15,7,20,3]))

