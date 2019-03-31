#
# @lc app=leetcode.cn id=119 lang=python
#
# [119] 杨辉三角 II
#
# https://leetcode-cn.com/problems/pascals-triangle-ii/description/
#
# algorithms
# Easy (53.78%)
# Total Accepted:    11.8K
# Total Submissions: 21.8K
# Testcase Example:  '3'
#
# 给定一个非负索引 k，其中 k ≤ 33，返回杨辉三角的第 k 行。
#
#
#
# 在杨辉三角中，每个数是它左上方和右上方的数的和。
#
# 示例:
#
# 输入: 3
# 输出: [1,3,3,1]
#
#
# 进阶：
#
# 你可以优化你的算法到 O(k) 空间复杂度吗？
#
#


class Solution(object):
    map_dict = {0: [1], 1: [1, 1]}

    def getRow(self, rowIndex):
        """
        :type rowIndex: int
        :rtype: List[int]
        """
        if rowIndex in Solution.map_dict:
            return Solution.map_dict[rowIndex]
        tmp = [1]
        for i in xrange(1, rowIndex):
            tmp.append(self.getRow(rowIndex-1)
                       [i-1] + self.getRow(rowIndex-1)[i])
        tmp.append(1)
        Solution.map_dict[rowIndex] = tmp
        return tmp

