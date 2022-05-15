#
# @lc app=leetcode.cn id=258 lang=python3
#
# [258] 各位相加
#
# https://leetcode-cn.com/problems/add-digits/description/
#
# algorithms
# Easy (62.09%)
# Total Accepted:    11.8K
# Total Submissions: 18.8K
# Testcase Example:  '38'
#
# 给定一个非负整数 num，反复将各个位上的数字相加，直到结果为一位数。
#
# 示例:
#
# 输入: 38
# 输出: 2
# 解释: 各位相加的过程为：3 + 8 = 11, 1 + 1 = 2。 由于 2 是一位数，所以返回 2。
#
#
# 进阶:
# 你可以不使用循环或者递归，且在 O(1) 时间复杂度内解决这个问题吗？
#
#
class SolutionA(object):
    def addDigits(self, num: int) -> int:
        """
        转字符串
        """
        def func(num):
            result = 0
            for i in str(num):
                result += int(i)
            if num > 10:
                return func(result)
            else:
                return result
        return func(num)

class SolutionB(object):
    def addDigits(self, num: int) -> int:
        """
        循环取余
        """

        while num > 9:
            total = 0
            while num > 0:
                total += num % 10
                num = num // 10
            num = total
        return num

class Solution(object):
    def addDigits(self, num: int) -> int:
        """
        纯数学法, 不懂
        """
        if num == 0:
            return 0
        return ((num - 1) % 9) + 1

s = Solution().addDigits(1234)
print(s)
