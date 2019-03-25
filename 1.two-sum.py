# -*- coding:utf-8 -*-

# @lc app=leetcode.cn id=1 lang=python3
#
# [1] 两数之和
#
# https://leetcode-cn.com/problems/two-sum/description/
#
# algorithms
# Easy (44.25%)
# Total Accepted:    234.2K
# Total Submissions: 529.2K
# Testcase Example:  '[2,7,11,15]\n9'
#
# 给定一个整数数组 nums 和一个目标值 target，请你在该数组中找出和为目标值的那 两个 整数，并返回他们的数组下标。
#
# 你可以假设每种输入只会对应一个答案。但是，你不能重复利用这个数组中同样的元素。
#
# 示例:
#
# 给定 nums = [2, 7, 11, 15], target = 9
#
# 因为 nums[0] + nums[1] = 2 + 7 = 9
# 所以返回 [0, 1]
#
#
#

# slow verison
# class Solution(object):
#     def twoSum(self, nums, target):
#         """
#         :type nums: List[int]
#         :type target: int
#         :rtype: List[int]
#         """
#         for i, ele in enumerate(nums):
#             try:
#                 if i == nums.index(target-ele):
#                     continue
#                 return [i, nums.index(target-ele)]
#             except ValueError:
#                 continue

class Solution:
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        tmp_dict = {e: index for index, e in enumerate(nums)}
        for index, e in enumerate(nums):
            t = target - e
            if t in tmp_dict and tmp_dict[t] != index:
                return [index, tmp_dict[t]]

if __name__ == "__main__":
    a = Solution().twoSum([2, 7, 11, 15], 9)
    print(a)
