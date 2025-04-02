#
# @lc app=leetcode.cn id=114 lang=python3
#
# [114] 二叉树展开为链表
#
# https://leetcode-cn.com/problems/flatten-binary-tree-to-linked-list/description/
#
# algorithms
# Medium (72.82%)
# Likes:    1098
# Dislikes: 0
# Total Accepted:    227.3K
# Total Submissions: 312.2K
# Testcase Example:  '[1,2,5,3,4,null,6]'
#
# 给你二叉树的根结点 root ，请你将它展开为一个单链表：
#
#
# 展开后的单链表应该同样使用 TreeNode ，其中 right 子指针指向链表中下一个结点，而左子指针始终为 null 。
# 展开后的单链表应该与二叉树 先序遍历 顺序相同。
#
#
#
#
# 示例 1：
#
#
# 输入：root = [1,2,5,3,4,null,6]
# 输出：[1,null,2,null,3,null,4,null,5,null,6]
#
#
# 示例 2：
#
#
# 输入：root = []
# 输出：[]
#
#
# 示例 3：
#
#
# 输入：root = [0]
# 输出：[0]
#
#
#
#
# 提示：
#
#
# 树中结点数在范围 [0, 2000] 内
# -100
#
#
#
#
# 进阶：你可以使用原地算法（O(1) 额外空间）展开这棵树吗？
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

class SolutionA:
    def flatten(self, root: Optional[TreeNode]) -> None:
        """
        Do not return anything, modify root in-place instead.
        """
        if not root:
            return

        left = self.flatten(root.left)  # 左侧展开
        right = self.flatten(root.right)  # 右侧展开
        # 后序位置操作, 将左侧接到右节点, 将右侧接到节点的末尾
        root.left = None
        root.right = left
        p = root
        while p.right:
            p = p.right
        p.right = right
        return root

class Solution:
    def flatten(self, root: Optional[TreeNode]) -> None:
        if not root:
            return
        if not root.left and not root.right:
            return root, root
        p = root
        for cur in (root.left, root.right):
            if cur:
                start, end = self.flatten(cur)
                p.left = None
                p.right = start
                p = end
        return root, p
# @lc code=end

null = None
ll = [1,null,2,3]
t = TreeNode(1)
t.right = TreeNode(2)
t.right.left = TreeNode(3)
# t = build_tree(ll)
print(t)
s, _ = Solution().flatten(t)
print(s)
print(t.right.left, t.right.right)
