#
# @lc app=leetcode.cn id=557 lang=python3
#
# [557] 反转字符串中的单词 III
#
# https://leetcode-cn.com/problems/reverse-words-in-a-string-iii/description/
#
# algorithms
# Easy (74.20%)
# Likes:    445
# Dislikes: 0
# Total Accepted:    240.7K
# Total Submissions: 324.5K
# Testcase Example:  `"Let's take LeetCode contest"`
#
# 给定一个字符串 s ，你需要反转字符串中每个单词的字符顺序，同时仍保留空格和单词的初始顺序。
#
#
#
# 示例 1：
#
#
# 输入：s = "Let's take LeetCode contest"
# 输出："s'teL ekat edoCteeL tsetnoc"
#
#
# 示例 2:
#
#
# 输入： s = "God Ding"
# 输出："doG gniD"
#
#
#
#
# 提示：
#
#
# 1 <= s.length <= 5 * 10^4
# s 包含可打印的 ASCII 字符。
# s 不包含任何开头或结尾空格。
# s 里 至少 有一个词。
# s 中的所有单词都用一个空格隔开。
#
#
#

# @lc code=start
class Solution:
    def reverseWords(self, s: str) -> str:
        """原地解法"""

        if len(s) < 2:
            return s
        s = list(s)
        begin = 0
        end = 0
        while end < len(s):
            if s[end] != ' ':
                end += 1
            else:
                self.reverseStringSlice(s, begin, end-1)
                end += 1
                begin = end
        self.reverseStringSlice(s, begin, end-1)
        return ''.join(s)

    @staticmethod
    def reverseStringSlice(s: list, i: int, j: int):
        while i < j:
            s[i], s[j] = s[j], s[i]
            i += 1
            j -= 1
# @lc code=end

