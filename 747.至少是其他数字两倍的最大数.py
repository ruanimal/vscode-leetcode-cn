#
# @lc app=leetcode.cn id=747 lang=python3
#
# [747] 至少是其他数字两倍的最大数
#
# https://leetcode-cn.com/problems/largest-number-at-least-twice-of-others/description/
#
# algorithms
# Easy (38.67%)
# Likes:    40
# Dislikes: 0
# Total Accepted:    9.4K
# Total Submissions: 24.3K
# Testcase Example:  '[0,0,0,1]'
#
# 在一个给定的数组nums中，总是存在一个最大元素 。
#
# 查找数组中的最大元素是否至少是数组中每个其他数字的两倍。
#
# 如果是，则返回最大元素的索引，否则返回-1。
#
# 示例 1:
#
#
# 输入: nums = [3, 6, 1, 0]
# 输出: 1
# 解释: 6是最大的整数, 对于数组中的其他整数,
# 6大于数组中其他元素的两倍。6的索引是1, 所以我们返回1.
#
#
#
#
# 示例 2:
#
#
# 输入: nums = [1, 2, 3, 4]
# 输出: -1
# 解释: 4没有超过3的两倍大, 所以我们返回 -1.
#
#
#
#
# 提示:
#
#
# nums 的长度范围在[1, 50].
# 每个 nums[i] 的整数范围在 [0, 99].
#
#
#

from comm import *
# @lc code=start

class SolutionA:
    def dominantIndex(self, nums: List[int]) -> int:
        """暴力模拟法
        """
        if not nums:
            return

        max_val = nums[0]
        max_idx = 0
        for idx, i in enumerate(nums):
            if i > max_val:
                max_val = i
                max_idx = idx

        for i in nums:
            if max_val == i:
                continue
            if max_val < i * 2:
                return -1
        return max_idx

class Solution:
    def dominantIndex(self, nums: List[int]) -> int:
        """遍历一次, 记录第一大和第二大"""
        if len(nums) == 1:
            return 0
        first, second = (0, 1) if nums[0] >= nums[1] else (1, 0)
        for i in range(2, len(nums)):
            if nums[i] >= nums[first]:
                first, second = i, first
            elif nums[i] >= nums[second]:
                second = i
            else:
                continue
        return first if (nums[first] >= nums[second] * 2) else -1

# @lc code=end

if __name__ == "__main__":
    s = Solution().dominantIndex([1,2,3,6])
    print(s)

