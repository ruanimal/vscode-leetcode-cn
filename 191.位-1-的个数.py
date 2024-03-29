#
# @lc app=leetcode.cn id=191 lang=python3
#
# [191] 位1的个数
#
# https://leetcode-cn.com/problems/number-of-1-bits/description/
#
# algorithms
# Easy (46.68%)
# Total Accepted:    15.9K
# Total Submissions: 32.1K
# Testcase Example:  '00000000000000000000000000001011'
#
# 编写一个函数，输入是一个无符号整数，返回其二进制表达式中数字位数为 ‘1’ 的个数（也被称为汉明重量）。
#
#
#
# 示例 1：
#
# 输入：00000000000000000000000000001011
# 输出：3
# 解释：输入的二进制串 00000000000000000000000000001011 中，共有三位为 '1'。
#
#
# 示例 2：
#
# 输入：00000000000000000000000010000000
# 输出：1
# 解释：输入的二进制串 00000000000000000000000010000000 中，共有一位为 '1'。
#
#
# 示例 3：
#
# 输入：11111111111111111111111111111101
# 输出：31
# 解释：输入的二进制串 11111111111111111111111111111101 中，共有 31 位为 '1'。
#
#
#
# 提示：
#
#
# 请注意，在某些语言（如
# Java）中，没有无符号整数类型。在这种情况下，输入和输出都将被指定为有符号整数类型，并且不应影响您的实现，因为无论整数是有符号的还是无符号的，其内部的二进制表示形式都是相同的。
# 在 Java 中，编译器使用二进制补码记法来表示有符号整数。因此，在上面的 示例 3 中，输入表示有符号整数 -3。
#
#
#
#
# 进阶:
# 如果多次调用这个函数，你将如何优化你的算法？
#
#
class SolutionA(object):
    bases = [2**i for i in range(32)]
    def hammingWeight(self, n: int) -> int:
        """
        暴力法
        """
        count = 0
        for i in self.bases:
            if n & i:
                count += 1
        return count

class Solution(object):
    def hammingWeight(self, n: int) -> int:
        """
        variable-precision SWAR 算法

        http://ponder.work/2020/08/01/variable-precision-SWAR-algorithm/
        """

        M1 = 0b01010101010101010101010101010101
        M2 = 0b00110011001100110011001100110011
        M3 = 0b00001111000011110000111100001111

        res = n
        res = (res & M1) + ((res >> 1) & M1)
        res = (res & M2) + ((res >> 2) & M2)
        res = (res & M3) + ((res >> 4) & M3)
        res = ((res * 0x01010101) & 0xFFFFFFFF) >> 24
        return res

