#
# @lc app=leetcode.cn id=507 lang=python3
#
# [507] 完美数
#
# https://leetcode-cn.com/problems/perfect-number/description/
#
# algorithms
# Easy (34.31%)
# Likes:    31
# Dislikes: 0
# Total Accepted:    5.4K
# Total Submissions: 15.3K
# Testcase Example:  '28'
#
# 对于一个 正整数，如果它和除了它自身以外的所有正因子之和相等，我们称它为“完美数”。
#
# 给定一个 正整数 n， 如果他是完美数，返回 True，否则返回 False
#
#
#
# 示例：
#
#
# 输入: 28
# 输出: True
# 解释: 28 = 1 + 2 + 4 + 7 + 14
#
#
#
#
# 注意:
#
# 输入的数字 n 不会超过 100,000,000. (1e8)
#
#
class Solution:
    def checkPerfectNumber(self, num: int) -> bool:
        """暴力法
        """
        if num == 1:
            return False

        tmp = 1
        i = 2
        while i * i < num:
            if num % i == 0:
                tmp += i
                rest = num / i
                if rest != i:
                    tmp += rest
            if tmp > num:
                # print(tmp, num)
                return False
            i += 1
        return tmp == num

if __name__ == "__main__":
    s = Solution().checkPerfectNumber(28)
    print(s)
    s = Solution().checkPerfectNumber(2)
    print(s)

