#
# @lc app=leetcode.cn id=34 lang=python3
#
# [34] 在排序数组中查找元素的第一个和最后一个位置
#
# https://leetcode-cn.com/problems/find-first-and-last-position-of-element-in-sorted-array/description/
#
# algorithms
# Medium (42.24%)
# Likes:    1653
# Dislikes: 0
# Total Accepted:    520.9K
# Total Submissions: 1.2M
# Testcase Example:  '[5,7,7,8,8,10]\n8'
#
# 给定一个按照升序排列的整数数组 nums，和一个目标值 target。找出给定目标值在数组中的开始位置和结束位置。
#
# 如果数组中不存在目标值 target，返回 [-1, -1]。
#
# 进阶：
#
#
# 你可以设计并实现时间复杂度为 O(log n) 的算法解决此问题吗？
#
#
#
#
# 示例 1：
#
#
# 输入：nums = [5,7,7,8,8,10], target = 8
# 输出：[3,4]
#
# 示例 2：
#
#
# 输入：nums = [5,7,7,8,8,10], target = 6
# 输出：[-1,-1]
#
# 示例 3：
#
#
# 输入：nums = [], target = 0
# 输出：[-1,-1]
#
#
#
# 提示：
#
#
# 0
# -10^9 
# nums 是一个非递减数组
# -10^9 
#
#
#

from comm import *

# @lc code=start
class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        if not nums:
            return [-1,-1]
        first = self.findFirst(nums, target)
        if first == -1:
            return [-1, -1]
        last = self.findLast(nums, target)
        return [first, last]

    @staticmethod
    def findLast(nums: List[int], target: int) -> int:
        left = 0
        right = len(nums)-1
        while left <= right:
            mid = (left+right) >> 1
            if nums[mid] <= target:
                left = mid + 1
            else:
                right = mid - 1
        if right == -1:
            return -1
        if nums[right] != target:
            return -1
        return right

    @staticmethod
    def findFirst(nums: List[int], target: int) -> int:
        left = 0
        right = len(nums)-1
        while left <= right:
            mid = (left+right) >> 1
            if nums[mid] >= target:
                right = mid - 1
            else:
                left = mid + 1
        if left == len(nums):
            return -1
        if nums[left] != target:
            return -1
        return left

# @lc code=end
s = Solution().searchRange(nums = [5,7,7,8,8,10], target = 8)
print(s)
s = Solution().searchRange(nums = [5,7,7,8,8,10], target = 6)
print(s)
