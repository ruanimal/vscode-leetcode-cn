#
# @lc app=leetcode.cn id=405 lang=python3
#
# [405] 数字转换为十六进制数
#
# https://leetcode-cn.com/problems/convert-a-number-to-hexadecimal/description/
#
# algorithms
# Easy (43.97%)
# Total Accepted:    2.8K
# Total Submissions: 6.3K
# Testcase Example:  '26'
#
# 给定一个整数，编写一个算法将这个数转换为十六进制数。对于负整数，我们通常使用 补码运算 方法。
#
# 注意:
#
#
# 十六进制中所有字母(a-f)都必须是小写。
# 十六进制字符串中不能包含多余的前导零。如果要转化的数为0，那么以单个字符'0'来表示；对于其他情况，十六进制字符串中的第一个字符将不会是0字符。 
# 给定的数确保在32位有符号整数范围内。
# 不能使用任何由库提供的将数字直接转换或格式化为十六进制的方法。
#
#
# 示例 1：
#
#
# 输入:
# 26
#
# 输出:
# "1a"
#
#
# 示例 2：
#
#
# 输入:
# -1
#
# 输出:
# "ffffffff"
#
#
#
class Solution(object):
    def toHex(self, num: int) -> str:
        """位运算
        """
        if num == 0:
            return '0'

        # mask to get last 32 bits
        mask = 0xFFFFFFFF
        num = num if num >= 0 else ~(num ^ mask)

        tmp = []
        while num > 0:
            tmp.append('{:x}'.format(num & 0xF))
            num = num >> 4
        tmp = tmp[::-1]
        return ''.join(tmp)

if __name__ == "__main__":
    s = Solution().toHex(-1)
    print(s)

