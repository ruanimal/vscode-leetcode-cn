#
# @lc app=leetcode.cn id=98 lang=python
#
# [98] 验证二叉搜索树
#
# Definition for a binary tree node.
from comm import *

# @lc code=start

class Solution(object):
    def isValidBST(self, root, min_val=float('-inf'), max_val=float('+inf')):
        """
        :type root: TreeNode
        :rtype: bool
        对于二叉搜索树来的遍历结果 [left-part, root, right-part] 来说

        对于每个节点必须满足 max(left-part) < root < min(right-part)

        """
        if root is None:
            return True
        if root.val <= min_val:
            return False
        if root.val >= max_val:
            return False
        return (self.isValidBST(root.left, min_val, min(root.val, max_val))
                and self.isValidBST(root.right, max(root.val, min_val), max_val))

# @lc code=end
