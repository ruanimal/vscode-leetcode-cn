#
# @lc app=leetcode.cn id=494 lang=python3
#
# [494] 目标和
#
# https://leetcode-cn.com/problems/target-sum/description/
#
# algorithms
# Medium (49.12%)
# Likes:    1132
# Dislikes: 0
# Total Accepted:    200.6K
# Total Submissions: 408.7K
# Testcase Example:  '[1,1,1,1,1]\n3'
#
# 给你一个整数数组 nums 和一个整数 target 。
#
# 向数组中的每个整数前添加 '+' 或 '-' ，然后串联起所有整数，可以构造一个 表达式 ：
#
#
# 例如，nums = [2, 1] ，可以在 2 之前添加 '+' ，在 1 之前添加 '-' ，然后串联起来得到表达式 "+2-1" 。
#
#
# 返回可以通过上述方法构造的、运算结果等于 target 的不同 表达式 的数目。
#
#
#
# 示例 1：
#
#
# 输入：nums = [1,1,1,1,1], target = 3
# 输出：5
# 解释：一共有 5 种方法让最终目标和为 3 。
# -1 + 1 + 1 + 1 + 1 = 3
# +1 - 1 + 1 + 1 + 1 = 3
# +1 + 1 - 1 + 1 + 1 = 3
# +1 + 1 + 1 - 1 + 1 = 3
# +1 + 1 + 1 + 1 - 1 = 3
#
#
# 示例 2：
#
#
# 输入：nums = [1], target = 1
# 输出：1
#
#
#
#
# 提示：
#
#
# 1
# 0
# 0
# -1000
#
#
#

from comm import *
# @lc code=start
class Solution_A:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        """
        回溯法, 超时
        """

        if len(nums) == 0:
            return 0
        self.res = 0
        self.backtrack(nums, 0, target)
        return self.res

    def backtrack(self, nums: List[int], level: int, remain: int) -> int:
        if level == len(nums):
            if remain == 0:
                self.res += 1
            return

        for i in (-1, 1):
            remain += i * nums[level]
            self.backtrack(nums, level+1, remain)
            remain -= i * nums[level]

class Solution_B:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        """
        回溯法, 加缓存
        """

        if len(nums) == 0:
            return 0
        self.memo = {}
        return self.backtrack(nums, 0, target)

    def backtrack(self, nums: List[int], level: int, remain: int) -> int:
        if level == len(nums):
            if remain == 0:
                return 1
            return 0

        if (level, remain) in self.memo:
            return self.memo[(level, remain)]
        res = 0
        for i in (-1, 1):
            remain += i * nums[level]
            res += self.backtrack(nums, level+1, remain)
            remain -= i * nums[level]
        self.memo[(level, remain)] = res
        return res

class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        """
        动态规划

        首先，如果我们把 nums 划分成两个子集 A 和 B，分别代表分配 + 的数和分配 - 的数，那么他们和 target 存在如下关系：

        sum(A) - sum(B) = target
        sum(A) = target + sum(B)
        sum(A) + sum(A) = target + sum(B) + sum(A)
        2 * sum(A) = target + sum(nums)
        综上，可以推出 sum(A) = (target + sum(nums)) / 2，也就是把原问题转化成：nums 中存在几个子集 A，使得 A 中元素的和为 (target + sum(nums)) / 2？

        表示 nums[:i+1] 凑出 j(target) 的方案
        if j-nums[i] >= 0
            dp[i][j] = dp[i-1][j] + dp[i-1][j-nums[i]]
        else:
            dp[i][j] = dp[i-1][j]
        """

        length = len(nums)
        if length == 0:
            return 0

        total = sum(nums)
        if (total < abs(target) or (total + target) % 2 == 1):
            return 0

        target = (target + total) // 2
        dp = [[0] * (target+1) for _ in range(length+1)]
        dp[0][0] = 1
        for i in range(1, length+1):
            for j in range(target+1):
                if j >= nums[i-1]: # 装得下
                    dp[i][j] = dp[i-1][j] + dp[i-1][j-nums[i-1]]
                else:
                    dp[i][j] = dp[i-1][j]
        return dp[-1][-1]
        # @lc code=end
s = Solution()
res = s.findTargetSumWays(nums = [1,1,1,1,1], target = 3)
print(res)
