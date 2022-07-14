#
# @lc app=leetcode.cn id=53 lang=python3
#
# [53] 最大子数组和
#
# https://leetcode-cn.com/problems/maximum-subarray/description/
#
# algorithms
# Easy (55.08%)
# Likes:    5078
# Dislikes: 0
# Total Accepted:    1.1M
# Total Submissions: 2M
# Testcase Example:  '[-2,1,-3,4,-1,2,1,-5,4]'
#
# 给你一个整数数组 nums ，请你找出一个具有最大和的连续子数组（子数组最少包含一个元素），返回其最大和。
#
# 子数组 是数组中的一个连续部分。
#
#
#
# 示例 1：
#
#
# 输入：nums = [-2,1,-3,4,-1,2,1,-5,4]
# 输出：6
# 解释：连续子数组 [4,-1,2,1] 的和最大，为 6 。
#
#
# 示例 2：
#
#
# 输入：nums = [1]
# 输出：1
#
#
# 示例 3：
#
#
# 输入：nums = [5,4,-1,7,8]
# 输出：23
#
#
#
#
# 提示：
#
#
# 1 <= nums.length <= 10^5
# -10^4 <= nums[i] <= 10^4
#
#
#
#
# 进阶：如果你已经实现复杂度为 O(n) 的解法，尝试使用更为精妙的 分治法 求解。
#
#

from comm import *
# @lc code=start
class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        """
        dp[i]: 以i为结尾的子数组的最大和

        dp[i] 有两种「选择」，要么与前面的相邻子数组连接，形成一个和更大的子数组；
        要么不与前面的子数组连接，自成一派，自己作为一个子数组。

        dp[i] = max(nums[i], dp[i-1]+nums[i])


        结果是max(dp[0], .. dp[i])
        """

        dp = [0 for _ in nums]
        dp[0] = nums[0]
        for i in range(1, len(nums)):
            dp[i] = max(nums[i], dp[i-1]+nums[i])
        # print(dp)
        return max(dp)
# @lc code=end

print(Solution().maxSubArray([-2, 1]))

