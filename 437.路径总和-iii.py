#
# @lc app=leetcode.cn id=437 lang=python3
#
# [437] 路径总和 III
#
# https://leetcode-cn.com/problems/path-sum-iii/description/
#
# algorithms
# Medium (57.64%)
# Likes:    1335
# Dislikes: 0
# Total Accepted:    165.6K
# Total Submissions: 291.8K
# Testcase Example:  '[10,5,-3,3,2,null,11,3,-2,null,1]\n8'
#
# 给定一个二叉树的根节点 root ，和一个整数 targetSum ，求该二叉树里节点值之和等于 targetSum 的 路径 的数目。
#
# 路径 不需要从根节点开始，也不需要在叶子节点结束，但是路径方向必须是向下的（只能从父节点到子节点）。
#
#
#
# 示例 1：
#
#
#
#
# 输入：root = [10,5,-3,3,2,null,11,3,-2,null,1], targetSum = 8
# 输出：3
# 解释：和等于 8 的路径有 3 条，如图所示。
#
#
# 示例 2：
#
#
# 输入：root = [5,4,8,11,null,13,4,7,2,null,null,5,1], targetSum = 22
# 输出：3
#
#
#
#
# 提示:
#
#
# 二叉树的节点个数的范围是 [0,1000]
# -10^9  
# -1000  
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
class SolutionA(object):
    def pathSum(self, root: TreeNode, targetSum: int) -> int:
        """暴力法
        """
        if not root:
            return 0
        return self.helper(root, targetSum) + self.pathSum(root.left, targetSum) + self.pathSum(root.right, targetSum)

    def helper(self, root: TreeNode, sum: int) -> int:
        """求以当前节点为起点的路径数目
        """

        if not root:
            return 0
        ans = 0
        if sum == root.val:
            ans += 1
        # print(root.val, ans)
        ans += self.helper(root.left, sum-root.val)
        ans += self.helper(root.right, sum-root.val)
        return ans


# TODO(rlj): 需要进一步理解.
from collections import defaultdict

class Solution(object):
    def pathSum(self, root, sum):
        """动态规划思想, 前缀和"""

        def helper(root, cursum):
            if not root:
                return
            cursum += root.val
            self.res += lookup[cursum - sum]
            lookup[cursum] += 1
            helper(root.left, cursum)
            helper(root.right, cursum)
            lookup[cursum] -= 1

        lookup = defaultdict(int)
        lookup[0] = 1
        self.res = 0
        helper(root, 0)
        return self.res
# @lc code=end

