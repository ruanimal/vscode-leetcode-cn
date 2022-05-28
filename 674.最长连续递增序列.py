#
# @lc app=leetcode.cn id=674 lang=python3
#
# [674] 最长连续递增序列
#
# https://leetcode-cn.com/problems/longest-continuous-increasing-subsequence/description/
#
# algorithms
# Easy (40.07%)
# Likes:    39
# Dislikes: 0
# Total Accepted:    7.6K
# Total Submissions: 18.7K
# Testcase Example:  '[1,3,5,4,7]'
#
# 给定一个未经排序的整数数组，找到最长且连续的的递增序列。
#
# 示例 1:
#
#
# 输入: [1,3,5,4,7]
# 输出: 3
# 解释: 最长连续递增序列是 [1,3,5], 长度为3。
# 尽管 [1,3,5,7] 也是升序的子序列, 但它不是连续的，因为5和7在原数组里被4隔开。
#
#
# 示例 2:
#
#
# 输入: [2,2,2,2,2]
# 输出: 1
# 解释: 最长连续递增序列是 [2], 长度为1。
#
#
# 注意：数组长度不会超过10000。
#
#

from comm import *
# @lc code=start
class Solution_A(object):
    def findLengthOfLCIS(self, nums: List[int]) -> int:
        """记录递增区间的长度"""

        if not nums:
            return 0

        max_count = 0
        count = 1
        for i in range(1, len(nums)):
            if nums[i-1] < nums[i]:
                count += 1
            else:
                max_count = max(max_count, count)
                count = 1
        max_count = max(max_count, count)
        return max_count


class Solution:
    def findLengthOfLCIS(self, nums: List[int]) -> int:
        """用两个指针表示递增序列区间
        """

        if len(nums) <= 1:
            return len(nums)

        i, j = 0, 1
        length = 1
        while j < len(nums):
            if nums[j-1] >= nums[j]:
                length = max(j-i, length)
                i = j
            j += 1
        return max(length, j-i)
# @lc code=end
