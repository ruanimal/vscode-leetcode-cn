#
# @lc app=leetcode.cn id=171 lang=python
#
# [171] Excel表列序号
#
class Solution(object):
    def titleToNumber(self, s):
        """
        :type s: str
        :rtype: int
        """
        trans_map = {i:idx+1 for idx, i in enumerate('ABCDEFGHIJKLMNOPQRSTUVWXYZ')}
        ret = 0
        for idx, i in enumerate(s):
            ret += trans_map[i] * (26 ** (len(s)-idx-1))
        return ret

if __name__ == "__main__":
    s = Solution().titleToNumber("AB")
    print(s)
