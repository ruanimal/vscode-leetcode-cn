#
# @lc app=leetcode.cn id=367 lang=python3
#
# [367] 有效的完全平方数
#
# https://leetcode-cn.com/problems/valid-perfect-square/description/
#
# algorithms
# Easy (39.64%)
# Total Accepted:    8K
# Total Submissions: 20K
# Testcase Example:  '16'
#
# 给定一个正整数 num，编写一个函数，如果 num 是一个完全平方数，则返回 True，否则返回 False。
#
# 说明：不要使用任何内置的库函数，如  sqrt。
#
# 示例 1：
#
# 输入：16
# 输出：True
#
# 示例 2：
#
# 输入：14
# 输出：False
#
#
#
class SolutionA:
    all_nums = {i**2: i for i in range(65536)}

    def isPerfectSquare(self, num: int) -> bool:
        """查表法
        """
        return num in self.all_nums

import math

class SolutionB:
    def isPerfectSquare(self, num: int) -> bool:
        """库函数pow法
        """
        pow = math.pow(num, 0.5)
        return int(pow) == pow

class Solution:
    def isPerfectSquare(self, num: int) -> bool:
        """二分查找法
        """

        left = 0
        right = 65536
        while left < right:
            mid = (left + right) >> 1
            if mid * mid < num:
                left = mid + 1
            else:
                right = mid
        return left * left == num

if __name__ == "__main__":
    s = Solution().isPerfectSquare(9)
    print(s)
