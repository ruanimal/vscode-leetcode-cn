#
# @lc app=leetcode.cn id=693 lang=python
#
# [693] 交替位二进制数
#
# https://leetcode-cn.com/problems/binary-number-with-alternating-bits/description/
#
# algorithms
# Easy (59.63%)
# Total Accepted:    5.1K
# Total Submissions: 8.6K
# Testcase Example:  '5'
#
# 给定一个正整数，检查他是否为交替位二进制数：换句话说，就是他的二进制数相邻的两个位数永不相等。
#
# 示例 1:
#
#
# 输入: 5
# 输出: True
# 解释:
# 5的二进制数是: 101
#
#
# 示例 2:
#
#
# 输入: 7
# 输出: False
# 解释:
# 7的二进制数是: 111
#
#
# 示例 3:
#
#
# 输入: 11
# 输出: False
# 解释:
# 11的二进制数是: 1011
#
#
# 示例 4:
#
#
# 输入: 10
# 输出: True
# 解释:
# 10的二进制数是: 1010
#
#
#
class Solution(object):
    bits = [2**i for i in range(32)]
    def hasAlternatingBits(self, n):
        """
        :type n: int
        :rtype: bool
        """
        pre = None
        for i in Solution.bits:
            if i > n:
                break
            if (n & i) == i:
                bit = 1
            else:
                bit = 0
            if pre is None:
                pre = bit
                continue
            else:
                if not (bit ^ pre):
                    return False
            pre = bit
        return True

if __name__ == "__main__":
    s = Solution().hasAlternatingBits(5)
    print(s)
