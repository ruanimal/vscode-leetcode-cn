#
# @lc app=leetcode.cn id=1005 lang=python3
#
# [1005] K 次取反后最大化的数组和
#
# https://leetcode-cn.com/problems/maximize-sum-of-array-after-k-negations/description/
#
# algorithms
# Easy (51.83%)
# Likes:    255
# Dislikes: 0
# Total Accepted:    85.1K
# Total Submissions: 165K
# Testcase Example:  '[4,2,3]\n1'
#
# 给你一个整数数组 nums 和一个整数 k ，按以下方法修改该数组：
#
#
# 选择某个下标 i 并将 nums[i] 替换为 -nums[i] 。
#
#
# 重复这个过程恰好 k 次。可以多次选择同一个下标 i 。
#
# 以这种方式修改数组后，返回数组 可能的最大和 。
#
#
#
# 示例 1：
#
#
# 输入：nums = [4,2,3], k = 1
# 输出：5
# 解释：选择下标 1 ，nums 变为 [4,-2,3] 。
#
#
# 示例 2：
#
#
# 输入：nums = [3,-1,0,2], k = 3
# 输出：6
# 解释：选择下标 (1, 2, 2) ，nums 变为 [3,1,0,2] 。
#
#
# 示例 3：
#
#
# 输入：nums = [2,-3,-1,5,-4], k = 2
# 输出：13
# 解释：选择下标 (1, 4) ，nums 变为 [2,3,-1,5,4] 。
#
#
#
#
# 提示：
#
#
# 1 <= nums.length <= 10^4
# -100 <= nums[i] <= 100
# 1 <= k <= 10^4
#
#
#

from comm import *
# @lc code=start
class Solution:
    def largestSumAfterKNegations(self, nums: List[int], k: int) -> int:
        if not nums or not k:
            return 0

        neg_nums = [i for i in nums if i < 0]
        pos_nums = [i for i in nums if i >= 0]
        neg_nums.sort()
        pos_nums.sort()
        if k <= len(neg_nums):  # 从小到大将负数变正数
            return -sum(neg_nums[:k]) + sum(neg_nums[k:]) + sum(pos_nums)
        k -= len(neg_nums)
        if k % 2 == 1:   # 奇数
            # 负数的最大值和正数的最小值二选一
            if pos_nums and neg_nums:
                return -sum(neg_nums[:-1]) + sum(pos_nums[1:]) + max(neg_nums[-1]+pos_nums[0], -neg_nums[-1]-pos_nums[0])
            elif pos_nums:  # 只有正数
                return -pos_nums[0] + sum(pos_nums[1:])
            else:
                return -sum(neg_nums[:-1]) + neg_nums[-1]
        # 偶数的话正反抵消了
        return -sum(neg_nums) + sum(pos_nums)

# @lc code=end

s = Solution().largestSumAfterKNegations([-8,3,-5,-3,-5,-2], 6)
print(s)
s = Solution().largestSumAfterKNegations([4, 2, 3], 1)
print(s)
