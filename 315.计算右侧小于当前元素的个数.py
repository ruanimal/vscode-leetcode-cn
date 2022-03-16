#
# @lc app=leetcode.cn id=315 lang=python3
#
# [315] 计算右侧小于当前元素的个数
#
# https://leetcode-cn.com/problems/count-of-smaller-numbers-after-self/description/
#
# algorithms
# Hard (41.95%)
# Likes:    761
# Dislikes: 0
# Total Accepted:    56.6K
# Total Submissions: 134.8K
# Testcase Example:  '[5,2,6,1]'
#
# 给你一个整数数组 nums ，按要求返回一个新数组 counts 。数组 counts 有该性质： counts[i] 的值是  nums[i] 右侧小于
# nums[i] 的元素的数量。
#
#
#
# 示例 1：
#
#
# 输入：nums = [5,2,6,1]
# 输出：[2,1,1,0]
# 解释：
# 5 的右侧有 2 个更小的元素 (2 和 1)
# 2 的右侧仅有 1 个更小的元素 (1)
# 6 的右侧有 1 个更小的元素 (1)
# 1 的右侧有 0 个更小的元素
#
#
# 示例 2：
#
#
# 输入：nums = [-1]
# 输出：[0]
#
#
# 示例 3：
#
#
# 输入：nums = [-1,-1]
# 输出：[0,0]
#
#
#
#
# 提示：
#
#
# 1 <= nums.length <= 10^5
# -10^4 <= nums[i] <= 10^4
#
#
#

# @lc code=start
class Solution:
    def countSmaller(self, nums: List[int]) -> List[int]:
        """暴力法, 时间超时"""

        if len(nums) == 0:
            return []

        length = len(nums)
        res = [0 for _ in nums]
        for i in range(length):
            for j in range(i+1, length):
                if nums[j] < nums[i]:
                    res[i] += 1
        return res

# @lc code=end

from comm import *
if __name__ == '__main__':
    s = Solution()
    r = s.countSmaller([5,2,6,1])
    print(r)
