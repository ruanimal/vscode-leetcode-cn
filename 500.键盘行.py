#
# @lc app=leetcode.cn id=500 lang=python
#
# [500] 键盘行
#
class Solution(object):
    def findWords(self, words):
        """
        :type words: List[str]
        :rtype: List[str]
        """
        letters_map = {}
        for i in 'qwertyuiopQWERTYUIOP':
            letters_map[i] = 1
        for i in 'asdfghjklASDFGHJKL':
            letters_map[i] = 2
        for i in 'zxcvbnmZXCVBNM':
            letters_map[i] = 3
        ret = []
        for word in words:
            if len(set(letters_map[i] for i in word)) == 1:
                ret.append(word)
        return ret

if __name__ == "__main__":
    s = Solution().findWords(["Hello", "Alaska", "Dad", "Peace"])
    print(s)
