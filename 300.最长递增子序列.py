#
# @lc app=leetcode.cn id=300 lang=python3
#
# [300] 最长递增子序列
#
# https://leetcode-cn.com/problems/longest-increasing-subsequence/description/
#
# algorithms
# Medium (52.84%)
# Likes:    2351
# Dislikes: 0
# Total Accepted:    470K
# Total Submissions: 887.1K
# Testcase Example:  '[10,9,2,5,3,7,101,18]'
#
# 给你一个整数数组 nums ，找到其中最长严格递增子序列的长度。
#
# 子序列 是由数组派生而来的序列，删除（或不删除）数组中的元素而不改变其余元素的顺序。例如，[3,6,2,7] 是数组 [0,3,1,6,2,2,7]
# 的子序列。
#
#
# 示例 1：
#
#
# 输入：nums = [10,9,2,5,3,7,101,18]
# 输出：4
# 解释：最长递增子序列是 [2,3,7,101]，因此长度为 4 。
#
#
# 示例 2：
#
#
# 输入：nums = [0,1,0,3,2,3]
# 输出：4
#
#
# 示例 3：
#
#
# 输入：nums = [7,7,7,7,7,7,7]
# 输出：1
#
#
#
#
# 提示：
#
#
# 1 <= nums.length <= 2500
# -10^4 <= nums[i] <= 10^4
#
#
#
#
# 进阶：
#
#
# 你能将算法的时间复杂度降低到 O(n log(n)) 吗?
#
#
#
from comm import *

# @lc code=start

class SolutionA:
    def lengthOfLIS(self, nums: List[int]) -> int:
        """
        暴力法, 超时
        """

        def dfs(nums, path, max_len, level):
            if level == len(nums):
                if len(path) == 0:
                    return 0
                tmp = 1
                for i in range(1, len(path)):
                    if nums[path[i-1]] < nums[path[i]]:
                        tmp += 1
                    else:
                        break
                # print(path, tmp)
                return tmp
            path.append(level)  # 选择当前点
            max_len = max(dfs(nums, path, max_len, level+1), max_len)
            path.pop()          # 不选择当前点
            max_len = max(dfs(nums, path, max_len, level+1), max_len)
            return max_len

        return dfs(nums, [], 0, 0)

class SolutionB:
    def lengthOfLIS(self, nums: List[int]) -> int:
        """
        动态规划法

        // 定义：dp[i] 表示以 nums[i] 这个数结尾的最长递增子序列的长度
        则 当 0 < j < i 时
        dp[i] =
            nums[i] > nums[j]: max(dp[j] + 1)
            nums[i] <= nums[j]: max(dp[j])
        """
        if len(nums) == 0:
            return 0

        dp = [1] * len(nums)
        for i in range(1, len(nums)):
            for j in range(i):
                if nums[j] < nums[i]:
                    dp[i] = max(dp[i], dp[j]+1)
        return max(dp)

class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        top = []
        for i in nums:
            pos = self.find_first(top, i)
            if pos == -1:
                top.append(i)
            else:
                top[pos] = i
        # print(top)
        return len(top)

    @staticmethod
    def find_first(nums: List[int], target: int) -> int:
        if len(nums) == 0:
            return -1
        left = 0
        right = len(nums)-1
        while left <= right:
            mid = (left+right) >> 1
            if nums[mid] < target:
                left = mid + 1
            else:
                right = mid - 1
        # print(nums, target, left)
        if left == len(nums):
            return -1
        return left

# @lc code=end
print(Solution().lengthOfLIS([4,10,4,3,3,8,9]))
print(SolutionA().lengthOfLIS([4,10,4,3,3,8,9]))
