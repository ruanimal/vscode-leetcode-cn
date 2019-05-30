#
# @lc app=leetcode.cn id=520 lang=python
#
# [520] 检测大写字母
#
class Solution(object):
    def detectCapitalUse(self, word):
        """
        :type word: str
        :rtype: bool
        """
        if len(word) == 1:
            return True
        if word[0].islower():
            return word[1:].islower()
        if word[1:].isupper() or word[1:].islower():
            return True
        return False

if __name__ == "__main__":
    s = Solution().detectCapitalUse('USA')
    print(s)
    s = Solution().detectCapitalUse('Leetcode')
    print(s)
