#
# @lc app=leetcode.cn id=70 lang=python3
#
# [70] 爬楼梯
#
# https://leetcode-cn.com/problems/climbing-stairs/description/
#
# algorithms
# Easy (44.01%)
# Total Accepted:    38.5K
# Total Submissions: 85.7K
# Testcase Example:  '2'
#
# 假设你正在爬楼梯。需要 n 阶你才能到达楼顶。
#
# 每次你可以爬 1 或 2 个台阶。你有多少种不同的方法可以爬到楼顶呢？
#
# 注意：给定 n 是一个正整数。
#
# 示例 1：
#
# 输入： 2
# 输出： 2
# 解释： 有两种方法可以爬到楼顶。
# 1.  1 阶 + 1 阶
# 2.  2 阶
#
# 示例 2：
#
# 输入： 3
# 输出： 3
# 解释： 有三种方法可以爬到楼顶。
# 1.  1 阶 + 1 阶 + 1 阶
# 2.  1 阶 + 2 阶
# 3.  2 阶 + 1 阶
#
#
#

class SolutionA(object):
    def climbStairs(self, n: int) -> int:
        """
        动态规划解法
        1. 最后一步可以是1级,也可以是2级, f(n) = f(n-1) + f(n-2) , n >=0
        2. f(0) = 1, f(1) = 1
        """
        f = {}
        f[0] = 1  # 这里的含义不明确
        f[1] = 1
        for i in range(2, n+1):
            f[i] = f[i-1] + f[i-2]
        return f[n]

class Solution(object):
    def climbStairs(self, n: int) -> int:
        """
        :type n: int
        :rtype: int

        动态规划解法, 去除额外空间占用
        也是斐波那契数列
        """
        if n < 2:
            return 1
        a = b = 1
        for _ in range(1, n):
            a, b = b, a + b
        return b



if __name__ == "__main__":
    s = Solution().climbStairs(22)
    print(s)
    s = Solution().climbStairs(22)
    print(s)
