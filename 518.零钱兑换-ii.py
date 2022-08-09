#
# @lc app=leetcode.cn id=518 lang=python3
#
# [518] 零钱兑换 II
#
# https://leetcode-cn.com/problems/coin-change-2/description/
#
# algorithms
# Medium (41.52%)
# Likes:    48
# Dislikes: 0
# Total Accepted:    1.9K
# Total Submissions: 4.4K
# Testcase Example:  '5\n[1,2,5]'
#
# 给定不同面额的硬币和一个总金额。写出函数来计算可以凑成总金额的硬币组合数。假设每一种面额的硬币有无限个。 
#
#
#
#
#
#
# 示例 1:
#
# 输入: amount = 5, coins = [1, 2, 5]
# 输出: 4
# 解释: 有四种方式可以凑成总金额:
# 5=5
# 5=2+2+1
# 5=2+1+1+1
# 5=1+1+1+1+1
#
#
# 示例 2:
#
# 输入: amount = 3, coins = [2]
# 输出: 0
# 解释: 只用面额2的硬币不能凑成总金额3。
#
#
# 示例 3:
#
# 输入: amount = 10, coins = [10]
# 输出: 1
#
#
#
#
# 注意:
#
# 你可以假设：
#
#
# 0 <= amount (总金额) <= 5000
# 1 <= coin (硬币面额) <= 5000
# 硬币种类不超过 500 种
# 结果符合 32 位符号整数
#
#
#

from functools import lru_cache
from comm import *
# @lc code=start

class Solution:
    def change(self, amount: int, coins: List[int]) -> int:
        """动态规划, 背包问题, 抄的答案"""

        # 以amount=10, coins=[2,3] 为例
        dp = [0] * (amount + 1)    # dp[x]: 拼成x的组合数
        dp[0] = 1   # 要凑成0, 只有一种情况
        for coin in coins:
            for i in range(amount - coin + 1):   # 0, 1, ... 8
                if dp[i]:
                    dp[i + coin] = dp[i + coin] + dp[i]   # 用这个coin的情况 + 不用这个coin的情况
        return dp[amount]

class SolutionA:
    def change(self, amount: int, coins: List[int]) -> int:
        """动态规划其实就是分类递归, 该解法复杂度还是太高

        dp[i][j]: 凑成i元时, 最后一个硬币面值是coins[j]的组合个数

        如, 金额为5时, 可选硬币为[1, 2, 5]
           5=5
           5=2+2+1
           5=2+1+1+1
           5=1+1+1+1+1

        即dp[5][1] = 3 = dp[4][1] + dp[4][2] + dp[4][5] = 2 + 1 + 0
          dp[5][2] = 0 = dp[3][2] + dp[3][5] = 0 + 0
          dp[5][5] = 1


        对于每种硬币j, 只要dp[i-coins[j]]的所有组合结尾类型k满足 coins[k] >= coins[j]
        则都可以加上一个硬币j凑成金额j, (大于等于的条件是为了不重复, 其实k>=j也是一样的)

        """

        dp = [[0 for _ in coins] for _ in range(amount+1)]
        for idx, i in enumerate(coins):
            if i <= amount:
                dp[i][idx] = 1

        for i in range(amount+1):
            for j in range(len(coins)):
                for k in range(j, len(coins)):
                    if i > coins[j]:
                        dp[i][j] += dp[i-coins[j]][k]
        # pprint(dp)
        return sum(dp[amount])

class SolutionB:
    def change(self, amount: int, coins: List[int]) -> int:
        """
        接着SolutionA, 从公式的累加可以看出, 这个存在一个后缀和优化方法

        可以把dp数组的定义改成

        dp[i][j]: 凑成i元时, 最后一个硬币面值大于等于coins[j]的组合个数
        则
            dp[i][j] = dp[i-coins[j]][j]
        """

        if amount == 0:
            return 1

        dp = [[0 for _ in coins] for _ in range(amount+1)]
        for idx, i in enumerate(coins):
            if i <= amount:
                dp[i][idx] = 1

        for i in range(amount+1):
            pre_val = 0
            for j in range(len(coins)-1, -1, -1):
                if i > coins[j]:
                    dp[i][j] += dp[i-coins[j]][j] + pre_val
                else:
                    dp[i][j] += pre_val
                pre_val = dp[i][j]
        # print(dp)
        return dp[amount][0]

class SolutionC:
    def change(self, amount: int, coins: List[int]) -> int:
        """
        接着SolutionB, 发现如果改变遍历顺序, 就可以少保留一个状态

        用整个dp数组代表pre_val
        """

        if amount == 0:
            return 1

        dp = [0 for _ in range(amount+1)]
        for j in range(len(coins)-1, -1, -1):
            for i in range(amount+1):
                if i == coins[j]:
                    dp[i] += 1
                elif i > coins[j]:
                    dp[i] += dp[i-coins[j]]
        return dp[amount]
# @lc code=end

if __name__ == "__main__":
    s = Solution().change(amount = 5, coins = [1, 2, 5])
    print(s)
    s = SolutionA().change(amount = 5, coins = [1, 2, 5])
    print(s)
    s = SolutionB().change(amount = 5, coins = [1, 2, 5])
    print(s)
    s = SolutionC().change(amount = 100, coins = [99, 1])
    print(s)
    s = SolutionC().change(amount = 5, coins = [1, 2, 5])
    print(s)

