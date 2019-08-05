#
# @lc app=leetcode.cn id=344 lang=python
#
# [344] 反转字符串
#
# https://leetcode-cn.com/problems/reverse-string/description/
#
# algorithms
# Easy (65.10%)
# Total Accepted:    42.7K
# Total Submissions: 65.2K
# Testcase Example:  '["h","e","l","l","o"]'
#
# 编写一个函数，其作用是将输入的字符串反转过来。输入字符串以字符数组 char[] 的形式给出。
#
# 不要给另外的数组分配额外的空间，你必须原地修改输入数组、使用 O(1) 的额外空间解决这一问题。
#
# 你可以假设数组中的所有字符都是 ASCII 码表中的可打印字符。
#
#
#
# 示例 1：
#
# 输入：["h","e","l","l","o"]
# 输出：["o","l","l","e","h"]
#
#
# 示例 2：
#
# 输入：["H","a","n","n","a","h"]
# 输出：["h","a","n","n","a","H"]
#
#


class Solution(object):
    def reverseString(self, s):
        """
        :type s: str
        :rtype: str
        """
        # # v1
        # if len(s) < 2:
        #     return s
        # i = 0
        # while i < len(s)/2:
        #     s[i], s[-i-1] = s[-i-1], s[i]
        #     i += 1
        # return s

        # v2
        if len(s) < 2:
            return s
        i = 0
        j = len(s) - 1
        while i < j:
            s[i], s[j] = s[j], s[i]
            i += 1
            j -= 1
        return s

if __name__ == "__main__":
    print(Solution().reverseString(["h", "e", "l", "l", "o", " "]))
