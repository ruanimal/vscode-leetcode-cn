#
# @lc app=leetcode.cn id=783 lang=python3
#
# [783] 二叉搜索树中的搜索
#
# https://leetcode-cn.com/problems/minimum-distance-between-bst-nodes/description/
#
# algorithms
# Easy (51.02%)
# Total Accepted:    2.3K
# Total Submissions: 4.5K
# Testcase Example:  '[4,2,6,1,3,null,null]'
#
# 给定一个二叉搜索树的根结点 root, 返回树中任意两节点的差的最小值。
#
# 示例：
#
#
# 输入: root = [4,2,6,1,3,null,null]
# 输出: 1
# 解释:
# 注意，root是树结点对象(TreeNode object)，而不是数组。
#
# 给定的树 [4,2,6,1,3,null,null] 可表示为下图:
#
# ⁠         4
# ⁠       /   \
# ⁠     2      6
# ⁠    / \
# ⁠   1   3
#
# 最小的差值是 1, 它是节点1和节点2的差值, 也是节点3和节点2的差值。
#
# 注意：
#
#
# 二叉树的大小范围在 2 到 100。
# 二叉树总是有效的，每个节点的值都是整数，且不重复。
#
#
#
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

from comm import *

class SolutionA(object):
    def minDiffInBST(self, root):
        """层次遍历, 过于复杂, 没有很好地利用BST性质
        """
        def tree_max(node):
            if node.right is None:
                return node.val
            m = tree_max(node.right)
            return m

        def tree_min(node):
            if node.left is None:
                return node.val
            m = tree_min(node.left)
            return m

        level = [root]
        min_abs = None
        while level:
            next_level = []
            for node in level:
                if not node.right and not node.left:
                    continue
                elif node.right and node.left:
                    next_level.append(node.right)
                    next_level.append(node.left)
                    node_abs = min(abs(node.val - tree_min(node.right)), abs(node.val - tree_max(node.left)))
                elif node.right:
                    next_level.append(node.right)
                    node_abs = abs(node.val - tree_min(node.right))
                else:
                    next_level.append(node.left)
                    node_abs = abs(node.val - tree_max(node.left))

                if min_abs is None:
                    min_abs = node_abs
                else:
                    min_abs = min(min_abs, node_abs)
            level = next_level
        return min_abs

# @lc code=start

class SolutionB:
    def minDiffInBST(self, root: TreeNode):
        """纯递归解法, 后序遍历, 用于加深对递归理解
        注意: 如果获取同级节点的结果则用返回值
              如果获取全局信息则用全局变量

        min(self.ans, root.val-lmax, rmin-root.val)
        """

        self.ans = float('inf')
        self.travese(root)
        return self.ans

    def travese(self, root: TreeNode):
        if not root:
            return float('inf'), float('-inf')
        lmin, lmax = self.travese(root.left)
        rmin, rmax = self.travese(root.right)
        self.ans = min(self.ans, root.val-lmax, rmin-root.val)
        return min(root.val, lmin), max(root.val, rmax)

class Solution:
    def minDiffInBST(self, root: TreeNode):
        """纯递归解法, 中序遍历"""
        self.pre = None
        self.ans = float('inf')
        self.travese(root)
        return self.ans

    def travese(self, root: TreeNode):
        if not root:
            return

        self.travese(root.left)
        if self.pre:
            self.ans = min(self.ans, root.val-self.pre.val)
        self.pre = root
        self.travese(root.right)

# @lc code=end
