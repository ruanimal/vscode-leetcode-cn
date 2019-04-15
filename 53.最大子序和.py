#
# @lc app=leetcode.cn id=53 lang=python
#
# [53] 最大子序和
#
# https://leetcode-cn.com/problems/maximum-subarray/description/
#
# algorithms
# Easy (43.55%)
# Total Accepted:    49.4K
# Total Submissions: 112.1K
# Testcase Example:  '[-2,1,-3,4,-1,2,1,-5,4]'
#
# 给定一个整数数组 nums ，找到一个具有最大和的连续子数组（子数组最少包含一个元素），返回其最大和。
#
# 示例:
#
# 输入: [-2,1,-3,4,-1,2,1,-5,4],
# 输出: 6
# 解释: 连续子数组 [4,-1,2,1] 的和最大，为 6。
#
#
# 进阶:
#
# 如果你已经实现复杂度为 O(n) 的解法，尝试使用更为精妙的分治法求解。
#
#
class Solution(object):
    def maxSubArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """

        if len(nums) == 0:
            return

        res = -2**31
        f_n = -1
        for i in nums:
            f_n = max(i, f_n + i)  # 单个子序列的和
            res = max(f_n, res)
        return res

if __name__ == "__main__":
    s = Solution().maxSubArray( [-2,1,-3,4,-1,2,1,-5,4])
    print(s)

