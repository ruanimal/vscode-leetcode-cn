#
# @lc app=leetcode.cn id=69 lang=python3
#
# [69] x 的平方根
#
# https://leetcode-cn.com/problems/sqrtx/description/
#
# algorithms
# Easy (34.46%)
# Total Accepted:    31K
# Total Submissions: 87.6K
# Testcase Example:  '4'
#
# 实现 int sqrt(int x) 函数。
#
# 计算并返回 x 的平方根，其中 x 是非负整数。
#
# 由于返回类型是整数，结果只保留整数的部分，小数部分将被舍去。
#
# 示例 1:
#
# 输入: 4
# 输出: 2
#
#
# 示例 2:
#
# 输入: 8
# 输出: 2
# 说明: 8 的平方根是 2.82842...,
# 由于返回类型是整数，小数部分将被舍去。
#
#
#

class Solution(object):
    def mySqrt(self, x: int) -> int:
        """
        二分查找
        """
        left = 0
        right = x
        while left < right:
            mid = (left + right) >> 1
            if mid ** 2 < x:
                left = mid + 1
            else:
                right = mid
        if left ** 2 == x:
            return left
        return left - 1


if __name__ == "__main__":
    s = Solution().mySqrt(8)
    print(s)
    s = Solution().mySqrt(9)
    print(s)
    s = Solution().mySqrt(0)
    print(s)


