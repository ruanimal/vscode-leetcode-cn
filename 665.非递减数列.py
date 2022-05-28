#
# @lc app=leetcode.cn id=665 lang=python3
#
# [665] 非递减数列
#
# https://leetcode-cn.com/problems/non-decreasing-array/description/
#
# algorithms
# Medium (27.28%)
# Likes:    670
# Dislikes: 0
# Total Accepted:    85.1K
# Total Submissions: 310.7K
# Testcase Example:  '[4,2,3]'
#
# 给你一个长度为 n 的整数数组 nums ，请你判断在 最多 改变 1 个元素的情况下，该数组能否变成一个非递减数列。
#
# 我们是这样定义一个非递减数列的： 对于数组中任意的 i (0 <= i <= n-2)，总满足 nums[i] <= nums[i + 1]。
#
#
#
# 示例 1:
#
#
# 输入: nums = [4,2,3]
# 输出: true
# 解释: 你可以通过把第一个 4 变成 1 来使得它成为一个非递减数列。
#
#
# 示例 2:
#
#
# 输入: nums = [4,2,1]
# 输出: false
# 解释: 你不能在只改变一个元素的情况下将其变为非递减数列。
#
#
#
#
# 提示：
#
#
#
# n == nums.length
# 1 <= n <= 10^4
# -10^5 <= nums[i] <= 10^5
#
#
#

from comm import *
# @lc code=start
class Solution:
    def checkPossibility(self, nums: List[int]) -> bool:
        """将已遍历的数字都处理成非递减, 并记录处理次数
        """
        length = len(nums)
        count = 0
        i = 1
        while i < length and count < 2:
            if nums[i-1] <= nums[i]:
                i += 1
                continue
            # 出现一个逆序数, 处理这个逆序数, 保证 nums[i-2], nums[i-1], nums[i] 非递减
            count += 1
            if (i-2>=0 and nums[i-2] > nums[i]):  # nums[i] < nums[i-2] <= nums[i-1]
                nums[i] = nums[i-1]
            else:                                 # nums[i-2] <= nums[i] <= nums[i-1]
                nums[i-1] = nums[i]
            i += 1
        return count < 2
# @lc code=end

