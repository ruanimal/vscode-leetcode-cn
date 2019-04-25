#
# @lc app=leetcode.cn id=728 lang=python
#
# [728] 自除数
#
class Solution(object):
    def selfDividingNumbers(self, left, right):
        """
        :type left: int
        :type right: int
        :rtype: List[int]
        """
        ret = []
        for i in range(left, right+1):
            num_str = str(i)
            for j in num_str:
                if j == '0':
                    break
                if i % int(j) != 0:
                    break
            else:
                ret.append(i)
        return ret


