#
# @lc app=leetcode.cn id=1030 lang=python3
#
# [1030] 距离顺序排列矩阵单元格
#
# https://leetcode-cn.com/problems/matrix-cells-in-distance-order/description/
#
# algorithms
# Easy (70.91%)
# Likes:    127
# Dislikes: 0
# Total Accepted:    43.5K
# Total Submissions: 61.3K
# Testcase Example:  '1\n2\n0\n0'
#
# 给定四个整数 row ,   cols ,  rCenter 和 cCenter 。有一个 rows x cols 的矩阵，你在单元格上的坐标是
# (rCenter, cCenter) 。
#
# 返回矩阵中的所有单元格的坐标，并按与 (rCenter, cCenter) 的 距离 从最小到最大的顺序排。你可以按 任何 满足此条件的顺序返回答案。
#
# 单元格(r1, c1) 和 (r2, c2) 之间的距离为|r1 - r2| + |c1 - c2|。
#
#
#
# 示例 1：
#
#
# 输入：rows = 1, cols = 2, rCenter = 0, cCenter = 0
# 输出：[[0,0],[0,1]]
# 解释：从 (r0, c0) 到其他单元格的距离为：[0,1]
#
#
# 示例 2：
#
#
# 输入：rows = 2, cols = 2, rCenter = 0, cCenter = 1
# 输出：[[0,1],[0,0],[1,1],[1,0]]
# 解释：从 (r0, c0) 到其他单元格的距离为：[0,1,1,2]
# [[0,1],[1,1],[0,0],[1,0]] 也会被视作正确答案。
#
#
# 示例 3：
#
#
# 输入：rows = 2, cols = 3, rCenter = 1, cCenter = 2
# 输出：[[1,2],[0,2],[1,1],[0,1],[1,0],[0,0]]
# 解释：从 (r0, c0) 到其他单元格的距离为：[0,1,1,2,2,3]
# 其他满足题目要求的答案也会被视为正确，例如 [[1,2],[1,1],[0,2],[1,0],[0,1],[0,0]]。
#
#
#
#
# 提示：
#
#
# 1 <= rows, cols <= 100
# 0 <= rCenter < rows
# 0 <= cCenter < cols
#
#
#

from comm import *
# @lc code=start
class SolutionA:
    def allCellsDistOrder(self, rows: int, cols: int,
                          rCenter: int, cCenter: int) -> List[List[int]]:
        """暴力法"""

        dis_map = {}
        for x in range(0, rows):
            for y in range(0, cols):
                dis_map[(x, y)] = abs(x-rCenter) + abs(y-cCenter)
        return [list(i[0]) for i in sorted(dis_map.items(), key=lambda i: i[1])]


class SolutionA1:
    def allCellsDistOrder(self, rows: int, cols: int,
                          rCenter: int, cCenter: int) -> List[List[int]]:
        """暴力法, 排序优化"""

        dis_map = {}
        max_dis = 0
        for x in range(0, rows):
            for y in range(0, cols):
                dis = abs(x-rCenter) + abs(y-cCenter)
                max_dis = max(dis, max_dis)
                dis_map.setdefault(dis, []).append((x, y))
        res = []
        for i in range(max_dis+1):
            res.extend(dis_map[i])
        return res


class SolutionB:
    """BFS 超时"""

    def allCellsDistOrder(self, rows: int, cols: int,
                          rCenter: int, cCenter: int) -> List[List[int]]:
        stack = [(rCenter, cCenter)]
        visited = set()
        res = []
        while stack:
            x, y = stack.pop(0)
            if (x, y) not in visited:
                visited.add((x,y))
                res.append([x,y])
            for i, j in [(x-1, y), (x+1, y), (x, y-1), (x, y+1)]:
                if 0 <= i < rows and 0 <= j < cols and (i, j) not in visited:
                    stack.append((i, j))
        return res


class SolutionC:
    """层次遍历
    Your runtime beats 5.61 % of python3 submissions
    """

    def allCellsDistOrder(self, rows: int, cols: int,
                          rCenter: int, cCenter: int) -> List[List[int]]:
        level = [(rCenter, cCenter)]
        visited = set(level)
        res = []
        while level:
            next_level = []
            res.extend(level)
            for (x, y) in level:
                for i, j in [(x-1, y), (x+1, y), (x, y-1), (x, y+1)]:
                    if 0 <= i < rows and 0 <= j < cols and (i, j) not in visited:
                        next_level.append((i, j))
                        visited.add((i, j))
            level = next_level
        return res


class SolutionD:
    def allCellsDistOrder(self, rows: int, cols: int,
                          rCenter: int, cCenter: int) -> List[List[int]]:
        """数学几何法"""

        x0, y0 = rCenter, cCenter
        res = [(x0, y0)]
        directions = [(1, 1), (1, -1), (-1, -1), (-1, 1)]
        maxDist = max(rCenter, rows - 1 - rCenter) + max(cCenter, cols - 1 - cCenter)
        for r in range(1, maxDist+1):   # 多少圈
            # 西北东南四个顶点
            points = [(x0-r, y0), (x0, y0+r), (x0+r, y0), (x0, y0-r)]
            for (x, y), (dx, dy) in zip(points, directions):   # 沿顶点扩展每个边
                for rr in range(r):   # 每条边多少个点
                    (x1, y1) = (x+dx*rr, y+dy*rr)
                    if 0 <= x1 < rows and 0 <= y1 < cols:
                        res.append((x1, y1))
        return res

Solution = SolutionA1
# @lc code=end
s = Solution().allCellsDistOrder(rows = 3, cols = 3, rCenter = 1, cCenter = 1)
print(s)
s = Solution().allCellsDistOrder(rows = 1, cols = 2, rCenter = 0, cCenter = 0)
print(s)
