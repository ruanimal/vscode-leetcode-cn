#
# @lc app=leetcode.cn id=824 lang=python
#
# [824] 山羊拉丁文
#
class Solution(object):
    def toGoatLatin(self, S):
        """
        :type S: str
        :rtype: str
        """
        ans = []
        for idx, word in enumerate(S.split()):
            tmp = ''
            if word[0].lower() in {'a', 'e', 'i', 'u', 'o'}:
                tmp += word
            else:
                tmp += (word[1:] + word[0])
            tmp += 'ma'
            tmp += ('a' * (idx+1))
            ans.append(tmp)
        return ' '.join(ans)

if __name__ == "__main__":
    s = Solution().toGoatLatin("I speak Goat Latin")
    print(s)
