#
# @lc app=leetcode.cn id=1009 lang=python
#
# [1009] 十进制整数的反码
#
class Solution(object):
    def bitwiseComplement(self, N):
        """
        :type N: int
        :rtype: int
        """
        # # V1
        # trans = {'0': '1', '1': '0'}
        # return int(''.join(trans[i] for i in bin(N)[2:]), 2)
        return 2**(len(bin(N))-2)-1-N

if __name__ == "__main__":
    s = Solution().bitwiseComplement(7)
    print(s)

