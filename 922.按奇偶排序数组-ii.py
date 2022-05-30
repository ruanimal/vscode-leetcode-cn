#
# @lc app=leetcode.cn id=922 lang=python3
#
# [922] 按奇偶排序数组 II
#
# https://leetcode-cn.com/problems/sort-array-by-parity-ii/description/
#
# algorithms
# Easy (71.36%)
# Likes:    240
# Dislikes: 0
# Total Accepted:    97.9K
# Total Submissions: 137.3K
# Testcase Example:  '[4,2,5,7]'
#
# 给定一个非负整数数组 nums，  nums 中一半整数是 奇数 ，一半整数是 偶数 。
#
# 对数组进行排序，以便当 nums[i] 为奇数时，i 也是 奇数 ；当 nums[i] 为偶数时， i 也是 偶数 。
#
# 你可以返回 任何满足上述条件的数组作为答案 。
#
#
#
# 示例 1：
#
#
# 输入：nums = [4,2,5,7]
# 输出：[4,5,2,7]
# 解释：[4,7,2,5]，[2,5,4,7]，[2,7,4,5] 也会被接受。
#
#
# 示例 2：
#
#
# 输入：nums = [2,3]
# 输出：[2,3]
#
#
#
#
# 提示：
#
#
# 2 <= nums.length <= 2 * 10^4
# nums.length 是偶数
# nums 中一半是偶数
# 0 <= nums[i] <= 1000
#
#
#
#
# 进阶：可以不使用额外空间解决问题吗？
#
#

from comm import *
# @lc code=start
class Solution:
    def sortArrayByParityII(self, nums: List[int]) -> List[int]:
        """暴力法
        可优化
        """

        if not nums:
            return
        i, j = 0, 1
        while i < len(nums) and j < len(nums):
            while (nums[i] % 2) == 0:
                i += 2
                if i >= len(nums):
                    return nums
            while (nums[j] % 2) == 1:
                j += 2
                if j >= len(nums):
                    return nums
            # print(i, j)
            nums[i], nums[j] = nums[j], nums[i]
        return nums
# @lc code=end

