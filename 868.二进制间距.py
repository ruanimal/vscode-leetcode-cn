#
# @lc app=leetcode.cn id=868 lang=python
#
# [868] 二进制间距
#
class Solution(object):
    def binaryGap(self, N):
        """
        :type N: int
        :rtype: int
        """
        ans = 0
        pre1 = None
        index = 0
        while N:
            if N & 1 == 1:
                if pre1 is None:
                    pre1 = index
                ans = max(index-pre1, ans)
                pre1 = index
            index += 1
            N = N >> 1
        return ans

if __name__ == "__main__":
    s = Solution().binaryGap(22)
    print(s)
