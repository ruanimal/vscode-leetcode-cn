#
# @lc app=leetcode.cn id=169 lang=python
#
# [169] 求众数
#
# https://leetcode-cn.com/problems/majority-element/description/
#
# algorithms
# Easy (56.58%)
# Total Accepted:    32K
# Total Submissions: 54.7K
# Testcase Example:  '[3,2,3]'
#
# 给定一个大小为 n 的数组，找到其中的众数。众数是指在数组中出现次数大于 ⌊ n/2 ⌋ 的元素。
#
# 你可以假设数组是非空的，并且给定的数组总是存在众数。
#
# 示例 1:
#
# 输入: [3,2,3]
# 输出: 3
#
# 示例 2:
#
# 输入: [2,2,1,1,1,2,2]
# 输出: 2
#
#
#


class Solution(object):
    def majorityElement(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        ## solution 1
        # 排序
        # 遍历一次数组
        # n = len(nums)
        # if n == 1 or (n == 2 and nums[0] == nums[1]):
        #     return nums[0]

        # nums.sort()
        # count = 1
        # for i in range(n-1):
        #     if nums[i] == nums[i+1]:
        #         count += 1
        #     else:
        #         count = 1
        #     if count > n/2.0:
        #         return nums[i]

        n = len(nums)
        if n == 1 or (n == 2 and nums[0] == nums[1]):
            return nums[0]

        count_map = {}
        for i in nums:
            v = count_map.get(i, 0) + 1
            if v > (n // 2):
                return i
            count_map[i] = v

