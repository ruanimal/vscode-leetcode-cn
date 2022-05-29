#
# @lc app=leetcode.cn id=812 lang=python3
#
# [812] 最大三角形面积
#
# https://leetcode-cn.com/problems/largest-triangle-area/description/
#
# algorithms
# Easy (63.56%)
# Likes:    173
# Dislikes: 0
# Total Accepted:    32.6K
# Total Submissions: 47.2K
# Testcase Example:  '[[0,0],[0,1],[1,0],[0,2],[2,0]]'
#
# 给定包含多个点的集合，从其中取三个点组成三角形，返回能组成的最大三角形的面积。
#
#
# 示例:
# 输入: points = [[0,0],[0,1],[1,0],[0,2],[2,0]]
# 输出: 2
# 解释:
# 这五个点如下图所示。组成的橙色三角形是最大的，面积为2。
#
#
#
#
# 注意:
#
#
# 3 <= points.length <= 50.
# 不存在重复的点。
# -50 <= points[i][j] <= 50.
# 结果误差值在 10^-6 以内都认为是正确答案。
#
#
#

from comm import *
# @lc code=start
class Solution:
    def largestTriangleArea(self, points: List[List[int]]) -> float:
        """暴力法, 求全组合
        S=(x1y2 + x2y3 + x3y1- x1y3 - x2y1 - x3y2) /2;
        """
        import itertools

        ans = 0
        for (x1, y1), (x2, y2), (x3, y3) in itertools.combinations(points, 3):
            tmp = abs((x1*y2 + x2*y3 + x3*y1 - x1*y3 - x2*y1 - x3*y2) / 2.0)
            ans = max(tmp, ans)
        return ans
# @lc code=end

