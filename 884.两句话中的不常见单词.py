#
# @lc app=leetcode.cn id=884 lang=python
#
# [884] 两句话中的不常见单词
#
class Solution(object):
    def uncommonFromSentences(self, A, B):
        """
        :type A: str
        :type B: str
        :rtype: List[str]
        """
        counts_map = {}
        for i in A.split():
            counts_map[i] = counts_map.get(i, 0) + 1
        for i in B.split():
            counts_map[i] = counts_map.get(i, 0) + 1
        return [k for k, v in counts_map.items() if v==1]

if __name__ == "__main__":
    s = Solution().uncommonFromSentences(A = "this apple is sweet", B = "this apple is sour")
    print(s)
