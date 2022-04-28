#
# @lc app=leetcode.cn id=35 lang=python3
#
# [35] 搜索插入位置
#
# https://leetcode-cn.com/problems/search-insert-position/description/
#
# algorithms
# Easy (42.57%)
# Total Accepted:    36.9K
# Total Submissions: 85.6K
# Testcase Example:  '[1,3,5,6]\n5'
#
# 给定一个排序数组和一个目标值，在数组中找到目标值，并返回其索引。如果目标值不存在于数组中，返回它将会被按顺序插入的位置。
#
# 你可以假设数组中无重复元素。
#
# 示例 1:
#
# 输入: [1,3,5,6], 5
# 输出: 2
#
#
# 示例 2:
#
# 输入: [1,3,5,6], 2
# 输出: 1
#
#
# 示例 3:
#
# 输入: [1,3,5,6], 7
# 输出: 4
#
#
# 示例 4:
#
# 输入: [1,3,5,6], 0
# 输出: 0
#
#
#

# left = right = None
# class Solution(object):
#     def searchInsert(self, nums, target):
#         """
#         :type nums: List[int]
#         :type target: int
#         :rtype: int
#         """
#         def binary_search_loop_version(array, k):
#             global left
#             global right

#             left = 0
#             right = len(array) - 1
#             while left <= right:
#                 mid = (left + right) // 2
#                 if array[mid] == k:
#                     return mid
#                 elif array[mid] > k:
#                     right = mid - 1
#                 else:
#                     left = mid + 1
#             return -1
#         ret = binary_search_loop_version(nums, target)
#         if ret == -1:
#             # nums.insert(left, target)
#             return left
#         else:
#             return ret

class Solution(object):
    def searchInsert(self, nums, target):
        """
        二分查找, 找大于等于target的区间(支持有重复元素)

        要记得left, right 构成的区间代表什么含义, 边界是怎么移动的, 最终会在什么位置
        """

        left = 0
        right = len(nums)-1
        while left < right:
            mid = (left + right) >> 1
            # (mid, right]
            if nums[mid] < target:
                left = mid + 1
            else:
                right = mid
        if left == len(nums) - 1 and nums[left] < target:
            left += 1
        return left


if __name__ == "__main__":
    print(Solution().searchInsert([1, 3, 5, 6], 2))
    print(Solution().searchInsert([1, 1, 1, 1, 3, 5, 6], 2))
    print(Solution().searchInsert([1, 1, 1, 1, 3, 5, 6], 1))
    print(Solution().searchInsert([1, 1, 1, 1, 3, 5, 6], 3))
    print(Solution().searchInsert([1, 1, 1, 1, 3, 5, 6], 0))
