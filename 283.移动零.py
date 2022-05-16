#
# @lc app=leetcode.cn id=283 lang=python3
#
# [283] 移动零
#
# https://leetcode-cn.com/problems/move-zeroes/description/
#
# algorithms
# Easy (52.38%)
# Total Accepted:    39.6K
# Total Submissions: 74.4K
# Testcase Example:  '[0,1,0,3,12]'
#
# 给定一个数组 nums，编写一个函数将所有 0 移动到数组的末尾，同时保持非零元素的相对顺序。
#
# 示例:
#
# 输入: [0,1,0,3,12]
# 输出: [1,3,12,0,0]
#
# 说明:
#
#
# 必须在原数组上操作，不能拷贝额外的数组。
# 尽量减少操作次数。
#
#
#

from comm import *
# @lc code=start


class SolutionA(object):
    def moveZeroes(self, nums: List[int]) -> None:
        """
        暴力法
        """
        end = len(nums) - 1
        x = 0
        while x < end:
            if nums[x] == 0:
                del nums[x]
                nums.append(0)
                x -= 1
                end -= 1
            x += 1

class Solution(object):
    def moveZeroes(self, nums: List[int]) -> None:
        """
        双指针法
        """

        p1 = 0   # 非0区间末尾
        p2 = 0   # 未判断区间开头
        while p2 < len(nums):
            if (nums[p2] != 0):
                nums[p1], nums[p2] = nums[p2], nums[p1]
                p1 += 1
            p2 += 1

# @lc code=end

nums = [0,1,0,3,12]
Solution().moveZeroes(nums)
print(nums)

