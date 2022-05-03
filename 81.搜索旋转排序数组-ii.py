#
# @lc app=leetcode.cn id=81 lang=python3
#
# [81] 搜索旋转排序数组 II
#
# https://leetcode-cn.com/problems/search-in-rotated-sorted-array-ii/description/
#
# algorithms
# Medium (41.36%)
# Likes:    586
# Dislikes: 0
# Total Accepted:    154.5K
# Total Submissions: 373.4K
# Testcase Example:  '[2,5,6,0,0,1,2]\n0'
#
# 已知存在一个按非降序排列的整数数组 nums ，数组中的值不必互不相同。
#
# 在传递给函数之前，nums 在预先未知的某个下标 k（0 <= k < nums.length）上进行了 旋转 ，使数组变为 [nums[k],
# nums[k+1], ..., nums[n-1], nums[0], nums[1], ..., nums[k-1]]（下标 从 0 开始
# 计数）。例如， [0,1,2,4,4,4,5,6,6,7] 在下标 5 处经旋转后可能变为 [4,5,6,6,7,0,1,2,4,4] 。
#
# 给你 旋转后 的数组 nums 和一个整数 target ，请你编写一个函数来判断给定的目标值是否存在于数组中。如果 nums 中存在这个目标值
# target ，则返回 true ，否则返回 false 。
#
# 你必须尽可能减少整个操作步骤。
#
#
#
# 示例 1：
#
#
# 输入：nums = [2,5,6,0,0,1,2], target = 0
# 输出：true
#
#
# 示例 2：
#
#
# 输入：nums = [2,5,6,0,0,1,2], target = 3
# 输出：false
#
#
#
# 提示：
#
#
# 1 <= nums.length <= 5000
# -10^4 <= nums[i] <= 10^4
# 题目数据保证 nums 在预先未知的某个下标上进行了旋转
# -10^4 <= target <= 10^4
#
#
#
#
# 进阶：
#
#
# 这是 搜索旋转排序数组 的延伸题目，本题中的 nums  可能包含重复元素。
# 这会影响到程序的时间复杂度吗？会有怎样的影响，为什么？
#
#
#
#
#

from comm import *
# @lc code=start
class Solution:
    def search(self, nums: List[int], target: int) -> bool:
        if len(nums) <= 1:
            return target in nums

        length = len(nums)
        left = 0
        right = len(nums) - 1
        offset = self.get_offset(nums)
        get_val = lambda i: nums[(i+offset) % length]
        while left <= right:
            mid = (left+right)>>1
            if get_val(mid) >= target:
                right = mid - 1
            else:
                left = mid + 1
        # print(offset, left)
        if left == len(nums):
            return False
        return get_val(left) == target

    @staticmethod
    def get_offset(nums: List[int]) -> int:
        """找逆序位置, 也就是最小值的位置"""

        if nums[0] < nums[-1]:
            return 0
        left = 0
        right = len(nums) - 1
        # [left, right] 代表包含最小值的区间
        # nums[left] == nums[right] 的情况, 移动左边界(移动右边界会使逆序消失)
        while left < right and nums[left] == nums[-1]:
            left += 1
        # nums[left] > nums[right]
        # 要保证每一轮循环, 区间性质一致
        while left < right:
            mid = (left + right) >> 1
            if nums[mid] > nums[right]:
                left = mid + 1
            else:
                right = mid
            # print(left, right)
        # 退出时 left == right, 且nums[left] 为原数组起点
        return left
# @lc code=end

# assert Solution().get_offset([4,5,6,7,0,1,2]) == 4
# assert Solution().get_offset([4,5,6,7]) == 0
# assert Solution().get_offset([3, 1]) == 1
# assert Solution().get_offset([2,5,6,0,0,1,2]) == 3
# assert Solution().get_offset([1, 0, 1, 1, 1]) == 1
# assert Solution().get_offset([1, 1, 1, 0, 1]) == 3

s = Solution().search(nums = [2,5,6,0,0,1,2], target = 0)
assert s == True
s = Solution().search(nums = [2,5,6,0,0,1,2], target = -1)
assert s == False
s = Solution().search(nums = [2,2,3,3,0,1,1], target = 0)
assert s == True
s = Solution().search(nums = [1, 0, 1, 1, 1], target = 0)
assert s == True
s = Solution().search(nums = [1, 1, 1, 0, 1], target = 0)
assert s == True
s = Solution().search(nums = [1, 1], target = 0)
assert s == False
s = Solution().search([2,2,2,3,2,2,2], 3)
assert s == True
s = Solution().search([9, 1, 2, 3, 4], 3)
assert s == True
s = Solution().search([9, 1], 1)
assert s == True
s = Solution().search([1,1,1,1,1,1,1,1,1,1,1,1,1,2,1,1,1,1,1], 2)
assert s == True
