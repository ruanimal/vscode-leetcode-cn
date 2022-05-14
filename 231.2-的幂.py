#
# @lc app=leetcode.cn id=231 lang=python3
#
# [231] 2的幂
#
# https://leetcode-cn.com/problems/power-of-two/description/
#
# algorithms
# Easy (43.97%)
# Total Accepted:    15.6K
# Total Submissions: 34.9K
# Testcase Example:  '1'
#
# 给定一个整数，编写一个函数来判断它是否是 2 的幂次方。
#
# 示例 1:
#
# 输入: 1
# 输出: true
# 解释: 2^0 = 1
#
# 示例 2:
#
# 输入: 16
# 输出: true
# 解释: 2^4 = 16
#
# 示例 3:
#
# 输入: 218
# 输出: false
#
#
class SolutionA(object):
    bits = {2**i for i in range(32)}
    def isPowerOfTwo(self, n: int) -> bool:
        """
        查表法
        """
        return n in self.bits

class SolutionB(object):
    def isPowerOfTwo(self, n: int) -> bool:
        """
        位运算法, 较快
        """

        count = 0
        while n > 0:
            if count > 1:
                return False
            if n & 1 == 1:
                count += 1
            n = n >> 1
        return count == 1

class SolutionC(object):
    def isPowerOfTwo(self, n: int) -> bool:
        """
        位运算法, 参考第191题

        并不需要计算所有位数, 慢了
        """

        if (n <= 0) :
            return False
        M1 = 0b01010101010101010101010101010101
        M2 = 0b00110011001100110011001100110011
        M3 = 0b00001111000011110000111100001111

        res = n
        res = (res & M1) + ((res >> 1) & M1)
        res = (res & M2) + ((res >> 2) & M2)
        res = (res & M3) + ((res >> 4) & M3)
        res = ((res * 0x01010101) & 0xFFFFFFFF) >> 24
        return res == 1

class Solution(object):
    def isPowerOfTwo(self, n: int) -> bool:
        """
        n & (n-1) 的使用, 可以消除最低位的一个1
        """
        if n <= 0:
            return False
        return (n & (n-1)) == 0

print(Solution().isPowerOfTwo(3))
