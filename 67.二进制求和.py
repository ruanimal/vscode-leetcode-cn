#
# @lc app=leetcode.cn id=67 lang=python3
#
# [67] 二进制求和
#
# https://leetcode-cn.com/problems/add-binary/description/
#
# algorithms
# Easy (47.14%)
# Likes:    197
# Dislikes: 0
# Total Accepted:    26.1K
# Total Submissions: 53.7K
# Testcase Example:  '"11"\n"1"'
#
# 给定两个二进制字符串，返回他们的和（用二进制表示）。
#
# 输入为非空字符串且只包含数字 1 和 0。
#
# 示例 1:
#
# 输入: a = "11", b = "1"
# 输出: "100"
#
# 示例 2:
#
# 输入: a = "1010", b = "1011"
# 输出: "10101"
#
#
class SolutionA(object):
    def addBinary(self, a: str, b: str) -> str:
        """
        暴力库函数法
        """
        if not a or not b:
            return
        return bin(int(a, 2) + int(b, 2))[2:]


class Solution(object):
    def addBinary(self, a: str, b: str) -> str:
        length = max(len(a), len(b))
        a = '0' * (length-len(a)) + a
        b = '0' * (length-len(b)) + b
        length = len(a)
        res = ['0'] * length
        i = length-1
        extra = '0'
        while i >= 0:
            if a[i] == b[i] == '1':
                res[i] = extra
                extra = '1'
            elif a[i] == b[i] == '0':
                res[i] = extra
                extra = '0'
            elif extra == '1':
                res[i] = '0'
                extra = '1'
            else:
                res[i] = '1'
                extra = '0'
            i -= 1
        if extra == '1':
            res.insert(0, '1')
        return ''.join(res)

if __name__ == '__main__':
    s = Solution().addBinary(a = "11", b = "1")
    print(s)
