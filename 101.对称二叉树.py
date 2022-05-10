#
# @lc app=leetcode.cn id=101 lang=python3
#
# [101] 对称二叉树
#
# https://leetcode-cn.com/problems/symmetric-tree/description/
#
# algorithms
# Easy (44.77%)
# Total Accepted:    27.3K
# Total Submissions: 59.6K
# Testcase Example:  '[1,2,2,3,4,4,3]'
#
# 给定一个二叉树，检查它是否是镜像对称的。
#
# 例如，二叉树 [1,2,2,3,4,4,3] 是对称的。
#
# ⁠   1
# ⁠  / \
# ⁠ 2   2
# ⁠/ \ / \
# 3  4 4  3
#
#
# 但是下面这个 [1,2,2,null,3,null,3] 则不是镜像对称的:
#
# ⁠   1
# ⁠  / \
# ⁠ 2   2
# ⁠  \   \
# ⁠  3    3
#
#
# 说明:
#
# 如果你可以运用递归和迭代两种方法解决这个问题，会很加分。
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

class SolutionA(object):
    def isSymmetric(self, root: TreeNode):
        """
        层次遍历
        """
        if not root:
            return True

        level = [root]
        while level:
            next_level = []
            for node in level:
                if not node:
                    continue
                next_level.append(node.left)
                next_level.append(node.right)
            if next_level:
                for i in range(len(next_level)//2):
                    a = next_level[i].val if next_level[i] else None
                    b = next_level[-i-1].val if next_level[-i-1] else None
                    if a != b:
                        return False
            level = next_level
        return True

class Solution(object):
    def isSymmetric(self, root: TreeNode):
        """递归法, 参考判断树相同"""
        if not root:
            return True
        return self.helper(root.left, root.right)

    def helper(self, root1: TreeNode, root2: TreeNode):
        if not root1 and not root2:
            return True
        if (root1 and root2 and root1.val == root2.val
            and self.helper(root1.left, root2.right) and self.helper(root1.right, root2.left)):
            return True
        return False

# @lc code=end

