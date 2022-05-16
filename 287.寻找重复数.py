#
# @lc app=leetcode.cn id=287 lang=python3
#
# [287] 寻找重复数
#
# https://leetcode-cn.com/problems/find-the-duplicate-number/description/
#
# algorithms
# Medium (65.16%)
# Likes:    1718
# Dislikes: 0
# Total Accepted:    232.4K
# Total Submissions: 358K
# Testcase Example:  '[1,3,4,2,2]'
#
# 给定一个包含 n + 1 个整数的数组 nums ，其数字都在 [1, n] 范围内（包括 1 和 n），可知至少存在一个重复的整数。
#
# 假设 nums 只有 一个重复的整数 ，返回 这个重复的数 。
#
# 你设计的解决方案必须 不修改 数组 nums 且只用常量级 O(1) 的额外空间。
#
#
#
# 示例 1：
#
#
# 输入：nums = [1,3,4,2,2]
# 输出：2
#
#
# 示例 2：
#
#
# 输入：nums = [3,1,3,4,2]
# 输出：3
#
#
#
#
# 提示：
#
#
# 1 <= n <= 10^5
# nums.length == n + 1
# 1 <= nums[i] <= n
# nums 中 只有一个整数 出现 两次或多次 ，其余整数均只出现 一次
#
#
#
#
# 进阶：
#
#
# 如何证明 nums 中至少存在一个重复的数字?
# 你可以设计一个线性级时间复杂度 O(n) 的解决方案吗？
#
#
#

from comm import *
# @lc code=start

class SolutionB:
    def findDuplicate(self, nums: List[int]) -> int:
        """
        原地排序法, 优化

        不对, 因为修改了原数组
        """

        i = 0
        while i < len(nums):
            if nums[nums[i]-1] != nums[i]:
                nums[nums[i]-1], nums[i] = nums[i], nums[nums[i]-1]
            else:
                if nums[i] != i+1:
                    break
                i += 1
        return nums[i]

class SolutionA:
    def findDuplicate(self, nums: List[int]) -> int:
        """数学法

        结果不对, 题目是至少存在一个重复, 而不是刚好存在一个重复"""
        total = len(nums) * (len(nums)-1) // 2
        return sum(nums) - total

class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        """
        快慢指针法
        """
        fast = slow = 0
        while True:
            slow = nums[slow]
            fast = nums[nums[fast]]
            if slow == fast:
                break
        slow = 0
        while slow != fast:
            slow = nums[slow]
            fast = nums[fast]
        return slow

# @lc code=end

