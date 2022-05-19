#
# @lc app=leetcode.cn id=447 lang=python3
#
# [447] 回旋镖的数量
#
# https://leetcode-cn.com/problems/number-of-boomerangs/description/
#
# algorithms
# Medium (66.45%)
# Likes:    236
# Dislikes: 0
# Total Accepted:    51.8K
# Total Submissions: 77.9K
# Testcase Example:  '[[0,0],[1,0],[2,0]]'
#
# 给定平面上 n 对 互不相同 的点 points ，其中 points[i] = [xi, yi] 。回旋镖 是由点 (i, j, k) 表示的元组
# ，其中 i 和 j 之间的距离和 i 和 k 之间的欧式距离相等（需要考虑元组的顺序）。
#
# 返回平面上所有回旋镖的数量。
#
#
# 示例 1：
#
#
# 输入：points = [[0,0],[1,0],[2,0]]
# 输出：2
# 解释：两个回旋镖为 [[1,0],[0,0],[2,0]] 和 [[1,0],[2,0],[0,0]]
#
#
# 示例 2：
#
#
# 输入：points = [[1,1],[2,2],[3,3]]
# 输出：2
#
#
# 示例 3：
#
#
# 输入：points = [[1,1]]
# 输出：0
#
#
#
#
# 提示：
#
#
# n == points.length
# 1 <= n <= 500
# points[i].length == 2
# -10^4 <= xi, yi <= 10^4
# 所有点都 互不相同
#
#
#

from comm import *
# @lc code=start
class Solution:
    def numberOfBoomerangs(self, points: List[List[int]]) -> int:
        ans = 0
        counts_map = {}
        for i in points:
            for j in points:
                x1, y1 = i
                x2, y2 = j
                dis = (x1-x2)**2 + (y1-y2)**2
                counts_map[dis] = counts_map.get(dis, 0) + 1
            for dis, count in counts_map.items():
                ans += count*(count-1)   # 该距离的点有count个, 可组成count*(count-1)个回旋镖
            counts_map = {}
        return ans
# @lc code=end

