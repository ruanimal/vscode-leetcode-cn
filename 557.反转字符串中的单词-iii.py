#
# @lc app=leetcode.cn id=557 lang=python
#
# [557] 反转字符串中的单词 III
#
class Solution(object):
    def reverseWords(self, s):
        """
        :type s: str
        :rtype: str
        """
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
    def reverseStringSlice(s, i, j):
        """
        :type s: str
        :rtype: str
        """
        while i < j:
            s[i], s[j] = s[j], s[i]
            i += 1
            j -= 1

if __name__ == "__main__":
    s = Solution().reverseWords("Let's take LeetCode contest ")
    print(repr(s))

