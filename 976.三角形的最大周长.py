#
# @lc app=leetcode.cn id=976 lang=python3
#
# [976] 三角形的最大周长
#
# https://leetcode-cn.com/problems/largest-perimeter-triangle/description/
#
# algorithms
# Easy (59.27%)
# Likes:    192
# Dislikes: 0
# Total Accepted:    67.6K
# Total Submissions: 115.1K
# Testcase Example:  '[2,1,2]'
#
# 给定由一些正数（代表长度）组成的数组 nums ，返回 由其中三个长度组成的、面积不为零的三角形的最大周长 。如果不能形成任何面积不为零的三角形，返回
# 0。
#
#
#
#
#
#
# 示例 1：
#
#
# 输入：nums = [2,1,2]
# 输出：5
#
#
# 示例 2：
#
#
# 输入：nums = [1,2,1]
# 输出：0
#
#
#
#
# 提示：
#
#
# 3 <= nums.length <= 10^4
# 1 <= nums[i] <= 10^6
#
#
#

from comm import *
# @lc code=start
class Solution:
    def largestPerimeter(self, nums: List[int]) -> int:
        """两边之和大于第三边, 两边只差小于第三边"""

        if len(nums) < 3:
            return

        nums.sort(reverse=True)
        for i in range(len(nums)-2):
            if (nums[i] - nums[i+2] < nums[i+1] ) and (nums[i+1] + nums[i+2] > nums[i]):
                return nums[i] + nums[i+2] + nums[i+1]
        return 0
# @lc code=end

