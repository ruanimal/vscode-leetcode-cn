#
# @lc app=leetcode.cn id=326 lang=python3
#
# [326] 3的幂
#
# https://leetcode-cn.com/problems/power-of-three/description/
#
# algorithms
# Easy (42.34%)
# Total Accepted:    14.9K
# Total Submissions: 34.7K
# Testcase Example:  '27'
#
# 给定一个整数，写一个函数来判断它是否是 3 的幂次方。
#
# 示例 1:
#
# 输入: 27
# 输出: true
#
#
# 示例 2:
#
# 输入: 0
# 输出: false
#
# 示例 3:
#
# 输入: 9
# 输出: true
#
# 示例 4:
#
# 输入: 45
# 输出: false
#
# 进阶：
# 你能不使用循环或者递归来完成本题吗？
#
#


class SolutionA(object):
    def isPowerOfThree(self, n: int) -> bool:
        """
        3 ** 19 = 1162261467, int32范围内最大的3的次方
        由于3是素数, 如果1162261467能被n整除, 说明n是3的0-19次幂, 否则不是.
        """
        return (n > 0 and 1162261467 % n == 0)

class Solution(object):
    nums = {3 ** i for i in range(20)}
    def isPowerOfThree(self, n: int) -> bool:
        """查表法"""
        return n in self.nums

