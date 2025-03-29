#
# @lc app=leetcode.cn id=113 lang=python3
#
# [113] 路径总和 II
#
# https://leetcode.cn/problems/path-sum-ii/description/
#
# algorithms
# Medium (63.77%)
# Likes:    1172
# Dislikes: 0
# Total Accepted:    459.3K
# Total Submissions: 720.2K
# Testcase Example:  '[5,4,8,11,null,13,4,7,2,null,null,5,1]\n22'
#
# 给你二叉树的根节点 root 和一个整数目标和 targetSum ，找出所有 从根节点到叶子节点 路径总和等于给定目标和的路径。
#
# 叶子节点 是指没有子节点的节点。
#
#
#
#
#
# 示例 1：
#
#
# 输入：root = [5,4,8,11,null,13,4,7,2,null,null,5,1], targetSum = 22
# 输出：[[5,4,11,2],[5,8,4,5]]
#
#
# 示例 2：
#
#
# 输入：root = [1,2,3], targetSum = 5
# 输出：[]
#
#
# 示例 3：
#
#
# 输入：root = [1,2], targetSum = 0
# 输出：[]
#
#
#
#
# 提示：
#
#
# 树中节点总数在范围 [0, 5000] 内
# -1000
# -1000
#
#
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


T = Optional[TreeNode]
LL = List[List[int]]

class Solution:
    def dfs(self, root: T, target: int, path: list[int], result: LL):
        if root is None:
            if target == 0 and path:
                result.append(path[:])
            return

        path.append(root.val)
        if root.left is None and root.right is None:
            self.dfs(None, target-root.val, path, result)
        if root.left:
            self.dfs(root.left, target-root.val, path, result)
        if root.right:
            self.dfs(root.right, target-root.val, path, result)
        path.pop()

    def pathSum(self, root: T, targetSum: int) -> LL:
        path = []
        result = []
        self.dfs(root, targetSum, path, result)
        return result

# @lc code=end

t = TreeNode(1)
# t.left = TreeNode(2)
s = Solution().pathSum(t, 1)
print(s)
