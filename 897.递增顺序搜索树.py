#
# @lc app=leetcode.cn id=897 lang=python3
#
# [897] 递增顺序搜索树
#
# https://leetcode-cn.com/problems/increasing-order-search-tree/description/
#
# algorithms
# Easy (74.18%)
# Likes:    281
# Dislikes: 0
# Total Accepted:    69.7K
# Total Submissions: 94K
# Testcase Example:  '[5,3,6,2,4,null,8,1,null,null,null,7,9]'
#
# 给你一棵二叉搜索树的 root ，请你 按中序遍历
# 将其重新排列为一棵递增顺序搜索树，使树中最左边的节点成为树的根节点，并且每个节点没有左子节点，只有一个右子节点。
#
#
#
# 示例 1：
#
#
# 输入：root = [5,3,6,2,4,null,8,1,null,null,null,7,9]
# 输出：[1,null,2,null,3,null,4,null,5,null,6,null,7,null,8,null,9]
#
#
# 示例 2：
#
#
# 输入：root = [5,1,7]
# 输出：[1,null,5,null,7]
#
#
#
#
# 提示：
#
#
# 树中节点数的取值范围是 [1, 100]
# 0 <= Node.val <= 1000
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

class SolutionA:
    def increasingBST(self, root: TreeNode, tail=None) -> TreeNode:
        # 纯递归解法, 比较难理解
        if not root:
            return tail
        r = self.increasingBST(root.left, root)
        root.left = None
        root.right = self.increasingBST(root.right, tail)
        return r

class Solution:
    def increasingBST(self, root: TreeNode) -> TreeNode:
        # 中序遍历
        def travese(node, ret=None):
            if ret is None:
                ret = []
            if not node:
                return
            travese(node.left, ret)
            node.left = None
            ret.append(node)
            travese(node.right, ret)
            return ret
        ret = travese(root)
        ret[-1].right = None   # 去除旧的右节点
        ans = ret[0]
        for i in range(len(ret)-1):
            ret[i].right = ret[i+1]
        return ans
# @lc code=end

