#
# @lc app=leetcode.cn id=204 lang=python3
#
# [204] 计数质数
#
# https://leetcode-cn.com/problems/count-primes/description/
#
# algorithms
# Easy (27.42%)
# Likes:    157
# Dislikes: 0
# Total Accepted:    19.6K
# Total Submissions: 69K
# Testcase Example:  '10'
#
# 统计所有小于非负整数 n 的质数的数量。
#
# 示例:
#
# 输入: 10
# 输出: 4
# 解释: 小于 10 的质数一共有 4 个, 它们是 2, 3, 5, 7 。
#
#
#
class Solution(object):
    def countPrimes(self, n: int) -> int:
        """
        筛法求素数

        依次去除已知素数的倍速

        从i * i, 开始是因为 1 * i 到 (i-1) * i, 都被之前的数筛过了
        """

        if n < 2:
            return 0

        is_primes = [1 for i in range(n)]
        is_primes[0] = is_primes[1] = 0
        for i in range(2, n//2+1):
            if is_primes[i]:
                for j in range(i*i, n, i):
                    is_primes[j] = 0
        return sum(is_primes)

if __name__ == "__main__":
    s = Solution().countPrimes(12)
    print(s)


