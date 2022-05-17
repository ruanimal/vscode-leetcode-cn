#
# @lc app=leetcode.cn id=389 lang=python3
#
# [389] 找不同
#
# https://leetcode-cn.com/problems/find-the-difference/description/
#
# algorithms
# Easy (54.07%)
# Total Accepted:    7.7K
# Total Submissions: 13.9K
# Testcase Example:  '"abcd"\n"abcde"'
#
# 给定两个字符串 s 和 t，它们只包含小写字母。
#
# 字符串 t 由字符串 s 随机重排，然后在随机位置添加一个字母。
#
# 请找出在 t 中被添加的字母。
#
#
#
# 示例:
#
# 输入：
# s = "abcd"
# t = "abcde"
#
# 输出：
# e
#
# 解释：
# 'e' 是那个被添加的字母。
#
#
#
class Solution(object):
    def findTheDifference(self, s: str, t: str) -> str:
        """异或法
        转化为只有一个数字出现了1次, 其他数字都出现2次, 求该数字
        """
        tmp = 0
        for i in (s + t):
            tmp ^= ord(i)
        return chr(tmp)

if __name__ == "__main__":
    s = Solution().findTheDifference('abcd', 'acbed')
    print(s)
