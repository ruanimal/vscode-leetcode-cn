#
# @lc app=leetcode.cn id=13 lang=python
#
# [13] 罗马数字转整数
#
# https://leetcode-cn.com/problems/roman-to-integer/description/
#
# algorithms
# Easy (56.62%)
# Total Accepted:    48.9K
# Total Submissions: 85.3K
# Testcase Example:  '"III"'
#
# 罗马数字包含以下七种字符: I， V， X， L，C，D 和 M。
#
# 字符          数值
# I             1
# V             5
# X             10
# L             50
# C             100
# D             500
# M             1000
#
# 例如， 罗马数字 2 写做 II ，即为两个并列的 1。12 写做 XII ，即为 X + II 。 27 写做  XXVII, 即为 XX + V +
# II 。
#
# 通常情况下，罗马数字中小的数字在大的数字的右边。但也存在特例，例如 4 不写做 IIII，而是 IV。数字 1 在数字 5 的左边，所表示的数等于大数 5
# 减小数 1 得到的数值 4 。同样地，数字 9 表示为 IX。这个特殊的规则只适用于以下六种情况：
#
#
# I 可以放在 V (5) 和 X (10) 的左边，来表示 4 和 9。
# X 可以放在 L (50) 和 C (100) 的左边，来表示 40 和 90。 
# C 可以放在 D (500) 和 M (1000) 的左边，来表示 400 和 900。
#
#
# 给定一个罗马数字，将其转换成整数。输入确保在 1 到 3999 的范围内。
#
# 示例 1:
#
# 输入: "III"
# 输出: 3
#
# 示例 2:
#
# 输入: "IV"
# 输出: 4
#
# 示例 3:
#
# 输入: "IX"
# 输出: 9
#
# 示例 4:
#
# 输入: "LVIII"
# 输出: 58
# 解释: L = 50, V= 5, III = 3.
#
#
# 示例 5:
#
# 输入: "MCMXCIV"
# 输出: 1994
# 解释: M = 1000, CM = 900, XC = 90, IV = 4.
#
#


class Solution(object):
    def romanToInt(self, s):
        """
        :type s: str
        :rtype: int
        从左到右将罗马字符转换为数字再相加, 遇到IV这种就减去两倍的I
        """
        num_map = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
        result = 0
        for i in range(len(s)-1):
            result += num_map[s[i]]
            if num_map[s[i]] < num_map[s[i+1]]:
                result -= 2*num_map[s[i]]
        result += num_map[s[-1]]
        return result

    # def IntToroman(self, num):
    #     num_list = [1000, 900, 500, 400, 100, 90, 50, 40, 10, 9, 5, 4, 1]
    #     num_map = {
    #         1: 'I',
    #         4: 'IV',
    #         5: 'V',
    #         9: 'IX',
    #         10: 'X',
    #         40: 'XL',
    #         50: 'L',
    #         90: 'XC',
    #         100: 'C',
    #         400: 'CD',
    #         500: 'D',
    #         900: 'CM',
    #         1000: 'M',
    #     }

    #     ans = []
    #     for i in num_list:
    #         if i > num:
    #             continue
    #         if num == 0:
    #             break
    #         a, num = divmod(num, i)
    #         ans.append(a * num_map[i])
    #     return ''.join(ans)

if __name__ == "__main__":
    obj = Solution()
    for i in range(1,6000):
        a = obj.IntToroman(i)
        b = obj.romanToInt(a)
        print(a,b)
        assert i == b

