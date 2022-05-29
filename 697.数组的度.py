#
# @lc app=leetcode.cn id=697 lang=python3
#
# [697] 数组的度
#
# https://leetcode-cn.com/problems/degree-of-an-array/description/
#
# algorithms
# Easy (45.29%)
# Likes:    64
# Dislikes: 0
# Total Accepted:    4K
# Total Submissions: 8.7K
# Testcase Example:  '[1,2,2,3,1]'
#
# 给定一个非空且只包含非负数的整数数组 nums, 数组的度的定义是指数组里任一元素出现频数的最大值。
#
# 你的任务是找到与 nums 拥有相同大小的度的最短连续子数组，返回其长度。
#
# 示例 1:
#
#
# 输入: [1, 2, 2, 3, 1]
# 输出: 2
# 解释:
# 输入数组的度是2，因为元素1和2的出现频数最大，均为2.
# 连续子数组里面拥有相同度的有如下所示:
# [1, 2, 2, 3, 1], [1, 2, 2, 3], [2, 2, 3, 1], [1, 2, 2], [2, 2, 3], [2, 2]
# 最短连续子数组[2, 2]的长度为2，所以返回2.
#
#
# 示例 2:
#
#
# 输入: [1,2,2,3,1,4,2]
# 输出: 6
#
#
# 注意:
#
#
# nums.length 在1到50,000区间范围内。
# nums[i] 是一个在0到49,999范围内的整数。
#
#
#

from comm import *
# @lc code=start
class Solution(object):
    def findShortestSubArray(self, nums: List[int]) -> int:
        """hash计数统计法
        """
        nums_map = {}
        for idx, num in enumerate(nums):
            nums_map.setdefault(num, []).append(idx)
        ans = 50000
        max_len = max(len(i) for i in nums_map.values())
        for _, v in nums_map.items():
            if len(v) == max_len:
                ans = min(ans, v[-1] - v[0] + 1)
        return ans

# @lc code=end

if __name__ == "__main__":
    s = Solution().findShortestSubArray([1,2,2,3,1,4,2])
    print(s)
    s = Solution().findShortestSubArray([1,2,2,3,1])
    print(s)

