#
# @lc app=leetcode.cn id=50 lang=python3
#
# [50] Pow(x, n)
#
# https://leetcode-cn.com/problems/powx-n/description/
#
# algorithms
# Medium (37.80%)
# Likes:    944
# Dislikes: 0
# Total Accepted:    283.4K
# Total Submissions: 749.1K
# Testcase Example:  '2.00000\n10'
#
# 实现 pow(x, n) ，即计算 x 的 n 次幂函数（即，x^n^ ）。
#
#
#
# 示例 1：
#
#
# 输入：x = 2.00000, n = 10
# 输出：1024.00000
#
#
# 示例 2：
#
#
# 输入：x = 2.10000, n = 3
# 输出：9.26100
#
#
# 示例 3：
#
#
# 输入：x = 2.00000, n = -2
# 输出：0.25000
# 解释：2^-2 = 1/2^2 = 1/4 = 0.25
#
#
#
#
# 提示：
#
#
# -100.0 < x < 100.0
# -2^31 <= n <= 2^31-1
# -10^4 <= x^n <= 10^4
#
#
#

# @lc code=start
class Solution:
    def myPow(self, x: float, n: int) -> float:
        """
        n 有两种情况 奇数 或者 偶数, 注意保存结果防止重复调用
        奇数 myPow(x, n//2) * myPow(x, n//2) * x
        偶数 myPow(x, n//2) * myPow(x, n//2)
        """

        if n < 0:
            x = 1 / x
            n = -n
        if n == 0:
            return 1
        if n == 1:
            return x
        n, flag = divmod(n, 2)
        tmp = self.myPow(x, n)
        return tmp * tmp * x if flag else tmp * tmp

# @lc code=end

s = Solution().myPow(x = 2.00000, n = -2)
print(s)
s = Solution().myPow(x = 0.00001, n = 2147483647)
print(s)
