#
# @lc app=leetcode.cn id=1022 lang=python3
#
# [1022] 从根到叶的二进制数之和
#
# https://leetcode.cn/problems/sum-of-root-to-leaf-binary-numbers/description/
#
# algorithms
# Easy (75.05%)
# Likes:    259
# Dislikes: 0
# Total Accepted:    65.3K
# Total Submissions: 87.1K
# Testcase Example:  '[1,0,1,0,1,0,1]'
#
# 给出一棵二叉树，其上每个结点的值都是 0 或 1 。每一条从根到叶的路径都代表一个从最高有效位开始的二进制数。
#
#
# 例如，如果路径为 0 -> 1 -> 1 -> 0 -> 1，那么它表示二进制数 01101，也就是 13 。
#
#
# 对树上的每一片叶子，我们都要找出从根到该叶子的路径所表示的数字。
#
# 返回这些数字之和。题目数据保证答案是一个 32 位 整数。
#
#
#
# 示例 1：
#
#
# 输入：root = [1,0,1,0,1,0,1]
# 输出：22
# 解释：(100) + (101) + (110) + (111) = 4 + 5 + 6 + 7 = 22
#
#
# 示例 2：
#
#
# 输入：root = [0]
# 输出：0
#
#
#
#
# 提示：
#
#
# 树中的节点数在 [1, 1000] 范围内
# Node.val 仅为 0 或 1 
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

class SolutionA:
    def __init__(self) -> None:
        self.total = 0

    def sumRootToLeaf(self, root: T, num: int=0) -> int:
        if not root:
            return 0

        num <<= 1
        num |= root.val
        if not root.left and not root.right:
            self.total += num
        if root.left:
            self.sumRootToLeaf(root.left, num)
        if root.right:
            self.sumRootToLeaf(root.right, num)
        return self.total

class Solution:
    def sumRootToLeaf(self, root: T, num: int=0) -> int:
        if not root:
            return 0

        num <<= 1
        num |= root.val
        if not root.left and not root.right:
            return num
        return self.sumRootToLeaf(root.left, num) + self.sumRootToLeaf(root.right, num)

class SolutionBad:
    def sumRootToLeaf(self, root: T, total: int=0, num: int=0) -> int:
        """total 是不必要的, 累加导致会重复叠加左枝的结果"""

        if not root:
            return 0

        num <<= 1
        num |= root.val
        if not root.left and not root.right:
            print(bin(num), num)
            return num
        print('#1', total)
        total += self.sumRootToLeaf(root.left, total, num)
        print('#2', total)
        total += self.sumRootToLeaf(root.right, total, num)
        print('#3', total)
        return total

# @lc code=end

t = TreeNode(1)
t.left = TreeNode(0)
t.right = TreeNode(1)
t.left.left = TreeNode(0)
t.left.right = TreeNode(1)
t.right.left = TreeNode(0)
t.right.right = TreeNode(1)

s = Solution().sumRootToLeaf(t)
print(s)
s = SolutionBad().sumRootToLeaf(t)
print(s)
