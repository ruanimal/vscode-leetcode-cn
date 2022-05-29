#
# @lc app=leetcode.cn id=896 lang=python3
#
# [896] 单调数列
#
# https://leetcode-cn.com/problems/monotonic-array/description/
#
# algorithms
# Easy (58.16%)
# Likes:    163
# Dislikes: 0
# Total Accepted:    69.3K
# Total Submissions: 119.7K
# Testcase Example:  '[1,2,2,3]'
#
# 如果数组是单调递增或单调递减的，那么它是 单调 的。
#
# 如果对于所有 i <= j，nums[i] <= nums[j]，那么数组 nums 是单调递增的。 如果对于所有 i <= j，nums[i]> =
# nums[j]，那么数组 nums 是单调递减的。
#
# 当给定的数组 nums 是单调数组时返回 true，否则返回 false。
#
#
#
#
#
#
# 示例 1：
#
#
# 输入：nums = [1,2,2,3]
# 输出：true
#
#
# 示例 2：
#
#
# 输入：nums = [6,5,4,4]
# 输出：true
#
#
# 示例 3：
#
#
# 输入：nums = [1,3,2]
# 输出：false
#
#
#
#
# 提示：
#
#
# 1 <= nums.length <= 10^5
# -10^5 <= nums[i] <= 10^5
#
#
#

from comm import *
# @lc code=start
class Solution:
    def isMonotonic(self, nums: List[int]) -> bool:
        """暴力法"""

        if len(nums) == 0:
            return
        if len(nums) == 1:
            return True
        pre_flag = None
        for i in range(0, len(nums)-1):
            flag = self.compare(nums[i], nums[i+1])
            if flag == 0:
                continue
            if pre_flag is None:
                pre_flag = flag
            elif pre_flag != flag:
                return False
        return True

    @staticmethod
    def compare(a, b):
        if a > b:
            return 1
        elif a < b:
            return -1
        else:
            return 0

if __name__ == "__main__":
    s = Solution().isMonotonic([1,2,2,3])
    print(s)
    s = Solution().isMonotonic([1, 3,2])
    print(s)
# @lc code=end

