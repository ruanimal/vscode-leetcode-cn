#
# @lc app=leetcode.cn id=637 lang=python3
#
# [637] 二叉树的层平均值
#
# https://leetcode-cn.com/problems/average-of-levels-in-binary-tree/description/
#
# algorithms
# Easy (69.36%)
# Likes:    344
# Dislikes: 0
# Total Accepted:    103.4K
# Total Submissions: 148.8K
# Testcase Example:  '[3,9,20,null,null,15,7]'
#
# 给定一个非空二叉树的根节点 root , 以数组的形式返回每一层节点的平均值。与实际答案相差 10^-5 以内的答案可以被接受。
#
#
#
# 示例 1：
#
#
#
#
# 输入：root = [3,9,20,null,null,15,7]
# 输出：[3.00000,14.50000,11.00000]
# 解释：第 0 层的平均值为 3,第 1 层的平均值为 14.5,第 2 层的平均值为 11 。
# 因此返回 [3, 14.5, 11] 。
#
#
# 示例 2:
#
#
#
#
# 输入：root = [3,9,20,15,7]
# 输出：[3.00000,14.50000,11.00000]
#
#
#
#
# 提示：
#
#
#
#
# 树中节点数量在 [1, 10^4] 范围内
# -2^31 <= Node.val <= 2^31 - 1
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

class Solution:
    def averageOfLevels(self, root: Optional[TreeNode]) -> List[float]:
        """层次遍历"""

        ans = []
        level = [root]
        while level:
            next_level = []
            tmp = 0.0
            for i in level:
                tmp += i.val
                if i.left:
                    next_level.append(i.left)
                if i.right:
                    next_level.append(i.right)
            ans.append(tmp/len(level))
            level = next_level
        return ans
# @lc code=end

