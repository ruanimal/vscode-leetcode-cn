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
        # ret = []
        # pre_i = i = 0
        # while i < len(s):
        #     if s[i] == ' ':
        #         ret.append(s[pre_i:i][::-1])
        #         pre_i = i+1
        #     i += 1
        # ret.append(s[pre_i:i][::-1])
        # return ' '.join(ret)
        return ' '.join(i[::-1] for i in s.split())

if __name__ == "__main__":
    s = Solution().reverseWords("Let's take LeetCode contest")
    print(s)

