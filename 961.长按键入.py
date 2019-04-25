#
# @lc app=leetcode.cn id=961 lang=python
#
# [961] 长按键入
#
class Solution(object):
    def repeatedNTimes(self, A):
        """
        :type A: List[int]
        :rtype: int
        """
        counts_map = {}
        for i in A:
            counts_map[i] = counts_map.get(i, 0) + 1
            if counts_map[i] >= 2:
                return i

