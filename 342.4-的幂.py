#
# @lc app=leetcode.cn id=342 lang=python
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
class Solution(object):
    powers = {1, 4, 16, 64, 256, 1024, 4096, 16384, 65536, 262144,
                1048576, 4194304, 16777216, 67108864, 268435456, 1073741824}
    def isPowerOfFour(self, num):
        """
        :type num: int
        :rtype: bool
        """
        return num in Solution.powers

