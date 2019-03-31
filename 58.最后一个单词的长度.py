#
# @lc app=leetcode.cn id=58 lang=python
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
class Solution(object):
    def lengthOfLastWord(self, s):
        """
        :type s: str
        :rtype: int

        """
        # 解法一: 遍历字符串, 记录每个子字符串的长度
        # if not s:
        #     return 0

        # last = 0
        # tmp = 0
        # in_space = False
        # for i in range(len(s)):
        #     if s[i] != ' ':
        #         in_space = False
        #         tmp += 1
        #     else:
        #         if in_space == False:
        #             last = tmp
        #             tmp = 0
        #         in_space = True
        # # print(last, tmp, in_space)
        # if tmp != 0:
        #     return tmp
        # return last

        """
        总共两个变量, 当前字符是否空格, 当前是否在单词中; 组合产生4种状态
        """


        if not s:
            return 0

        count = 0
        in_word = False if (s[-1] == ' ') else True
        is_space = False
        for i in range(len(s)-1, -1, -1):
            is_space = (s[i] == ' ')
            if in_word and is_space:
                in_word = False
                break
            elif in_word and not is_space:
                count += 1
            elif not in_word and is_space:
                continue
            else:
                count = 1  # 第一个字符
                in_word = True
        return count


if __name__ == "__main__":
    print(Solution().lengthOfLastWord('  hello  world   '))
