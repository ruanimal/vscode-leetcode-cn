#
# @lc app=leetcode.cn id=58 lang=python3
#
# [58] 最后一个单词的长度
#
# https://leetcode-cn.com/problems/length-of-last-word/description/
#
# algorithms
# Easy (28.67%)
# Total Accepted:    21.7K
# Total Submissions: 74.2K
# Testcase Example:  '"Hello World"'
#
# 给定一个仅包含大小写字母和空格 ' ' 的字符串，返回其最后一个单词的长度。
#
# 如果不存在最后一个单词，请返回 0 。
#
# 说明：一个单词是指由字母组成，但不包含任何空格的字符串。
#
# 示例:
#
# 输入: "Hello World"
# 输出: 5
#
#
#

class SolutionA(object):
    def lengthOfLastWord(self, s):
        """
        :type s: str
        :rtype: int

        暴力法: 遍历字符串, 记录每个子字符串的长度
        """
        if not s:
            return 0

        last = 0
        tmp = 0
        in_space = False
        for i in range(len(s)):
            if s[i] != ' ':
                in_space = False
                tmp += 1
            else:
                if in_space == False:
                    last = tmp
                    tmp = 0
                in_space = True
        # print(last, tmp, in_space)
        if tmp != 0:
            return tmp
        return last

class Solution(object):
    def lengthOfLastWord(self, s):
        """
        :type s: str
        :rtype: int

        反向遍历, 同时简化状态
        如果末尾的是空格, 左移一位, 直到以字符开头
        """


        if not s:
            return 0

        i = len(s) - 1
        SPACE = ' '
        while i >= 0 and s[i] == SPACE:
            i -= 1
        count = 0
        while i >= 0 and s[i] != SPACE:
            count += 1
            i -= 1
        return count


if __name__ == "__main__":
    print(SolutionA().lengthOfLastWord('  hello  world   '))
