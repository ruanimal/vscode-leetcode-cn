#
# @lc app=leetcode.cn id=559 lang=python3
#
# [559] N叉树的最大深度
#
# https://leetcode-cn.com/problems/maximum-depth-of-n-ary-tree/description/
#
# algorithms
# Easy (66.74%)
# Likes:    47
# Dislikes: 0
# Total Accepted:    8.7K
# Total Submissions: 13K
# Testcase Example:  '{"$id":"1","children":[{"$id":"2","children":[{"$id":"5","children":[],"val":5},{"$id":"6","children":[],"val":6}],"val":3},{"$id":"3","children":[],"val":2},{"$id":"4","children":[],"val":4}],"val":1}'
#
# 给定一个 N 叉树，找到其最大深度。
#
# 最大深度是指从根节点到最远叶子节点的最长路径上的节点总数。
#
# 例如，给定一个 3叉树 :
#
#
#
#
#
#
#
# 我们应返回其最大深度，3。
#
# 说明:
#
#
# 树的深度不会超过 1000。
# 树的节点总不会超过 5000。
#
#

# @lc code=start

class Node:
    def __init__(self, val, children):
        self.val = val
        self.children = children

class Solution:
    def maxDepth(self, root: None) -> int:
        """递归法"""

        if not root:
            return 0

        max_depth = 1
        for i in root.children:
            max_depth = max(max_depth, 1 + self.maxDepth(i))
        return max_depth

# @lc code=end

