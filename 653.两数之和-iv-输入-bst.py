#
# @lc app=leetcode.cn id=653 lang=python3
#
# [653] 两数之和 IV - 输入 BST
#
# https://leetcode-cn.com/problems/two-sum-iv-input-is-a-bst/description/
#
# algorithms
# Easy (60.50%)
# Likes:    397
# Dislikes: 0
# Total Accepted:    91.8K
# Total Submissions: 145.4K
# Testcase Example:  '[5,3,6,2,4,null,7]\n9'
#
# 给定一个二叉搜索树 root 和一个目标结果 k，如果 BST 中存在两个元素且它们的和等于给定的目标结果，则返回 true。
#
#
#
# 示例 1：
#
#
# 输入: root = [5,3,6,2,4,null,7], k = 9
# 输出: true
#
#
# 示例 2：
#
#
# 输入: root = [5,3,6,2,4,null,7], k = 28
# 输出: false
#
#
#
#
# 提示:
#
#
# 二叉树的节点个数的范围是  [1, 10^4].
# -10^4 <= Node.val <= 10^4
# root 为二叉搜索树
# -10^5 <= k <= 10^5
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
    def findTarget(self, root: Optional[TreeNode], k: int) -> bool:
        """遍历二叉树, 转化为twosum问题"""

        def traverse(root):
            if not root:
                return
            nodes_map[root.val] = id(root)
            traverse(root.left)
            traverse(root.right)

        nodes_map = {}
        traverse(root)
        for key, val in nodes_map.items():
            # 防止某个节点被使用两次
            if (k - key) in nodes_map and nodes_map[k - key] != val:
                return True
        return False


class SolutionB:
    def findTarget(self, root: Optional[TreeNode], k: int) -> bool:
        """中序遍历, 双指针"""

        def traverse(root):
            if not root:
                return
            traverse(root.left)
            nums.append(root.val)
            traverse(root.right)

        nums = []
        traverse(root)

        if len(nums) < 2:
            return False
        i = 0
        j = len(nums)-1
        while i < j:
            tmp = nums[i] + nums[j]
            if tmp == k:
                return True
            elif tmp > k:
                j -= 1
            else:
                i += 1
        return False

class Solution:
    def __init__(self) -> None:
        self.s = set()

    def findTarget(self, root: Optional[TreeNode], k: int) -> bool:
        """遍历的同时做判断"""
        if root is None:
            return False
        if (k - root.val) in self.s:
            return True
        self.s.add(root.val)
        return self.findTarget(root.left, k) or self.findTarget(root.right, k)

# @lc code=end

