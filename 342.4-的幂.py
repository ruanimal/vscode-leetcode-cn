#
# @lc app=leetcode.cn id=342 lang=python3
#
# [342] 4的幂
#
# https://leetcode-cn.com/problems/power-of-four/description/
#
# algorithms
# Easy (44.12%)
# Total Accepted:    6.5K
# Total Submissions: 14.6K
# Testcase Example:  '16'
#
# 给定一个整数 (32 位有符号整数)，请编写一个函数来判断它是否是 4 的幂次方。
#
# 示例 1:
#
# 输入: 16
# 输出: true
#
#
# 示例 2:
#
# 输入: 5
# 输出: false
#
# 进阶：
# 你能不使用循环或者递归来完成本题吗？
#
#
class SolutionA(object):
    powers = {4 ** i for i in range(16)}
    def isPowerOfFour(self, num: int) -> bool:
        """查表法
        4 ** 15 == 1073741824, 是int32范围内的4的最次方
        """
        return num in self.powers


class SolutionB(object):
    def isPowerOfFour(self, num: int) -> bool:
        """暴力法, 超时
        4 ** 15 == 1073741824, 是int32范围内的4的最次方
        """
        while (num & 0b11) == 0:
            num >>= 2
        return num == 1

class Solution(object):
    def isPowerOfFour(self, num: int) -> bool:
        """二进制法
        只有一个1, 而且1的位置出现在1, 3, 5...的位置上
        """

        mask = 0b01010101010101010101010101010101
        return  num > 0 and (num & mask) == num and (num & (num-1)) == 0
s = Solution().isPowerOfFour(16)
print(s)
