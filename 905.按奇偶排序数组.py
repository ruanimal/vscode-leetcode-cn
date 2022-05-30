#
# @lc app=leetcode.cn id=905 lang=python3
#
# [905] 按奇偶排序数组
#
# https://leetcode-cn.com/problems/sort-array-by-parity/description/
#
# algorithms
# Easy (70.00%)
# Likes:    316
# Dislikes: 0
# Total Accepted:    106.6K
# Total Submissions: 149.6K
# Testcase Example:  '[3,1,2,4]'
#
# 给你一个整数数组 nums，将 nums 中的的所有偶数元素移动到数组的前面，后跟所有奇数元素。
#
# 返回满足此条件的 任一数组 作为答案。
#
#
#
# 示例 1：
#
#
# 输入：nums = [3,1,2,4]
# 输出：[2,4,3,1]
# 解释：[4,2,3,1]、[2,4,1,3] 和 [4,2,1,3] 也会被视作正确答案。
#
#
# 示例 2：
#
#
# 输入：nums = [0]
# 输出：[0]
#
#
#
#
# 提示：
#
#
# 1 <= nums.length <= 5000
# 0 <= nums[i] <= 5000
#
#
#

from comm import *
# @lc code=start
class Solution:
    def sortArrayByParity(self, nums: List[int]) -> List[int]:
        """
        参考快排
        """
        i = 0
        j = len(nums) - 1
        is_even = lambda i: (i & 1) == 0
        while i < j:
            if is_even(nums[i]):
                i += 1
                continue
            if not is_even(nums[j]):
                j -= 1
                continue
            nums[i], nums[j] = nums[j], nums[i]
        return nums

# @lc code=end

