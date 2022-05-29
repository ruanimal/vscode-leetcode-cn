#
# @lc app=leetcode.cn id=892 lang=python3
#
# [892] 三维形体的表面积
#
# https://leetcode-cn.com/problems/surface-area-of-3d-shapes/description/
#
# algorithms
# Easy (63.89%)
# Likes:    160
# Dislikes: 0
# Total Accepted:    35.3K
# Total Submissions: 55.3K
# Testcase Example:  '[[2]]'
#
# 给你一个 n * n 的网格 grid ，上面放置着一些 1 x 1 x 1 的正方体。每个值 v = grid[i][j] 表示 v
# 个正方体叠放在对应单元格 (i, j) 上。
#
# 放置好正方体后，任何直接相邻的正方体都会互相粘在一起，形成一些不规则的三维形体。
#
# 请你返回最终这些形体的总表面积。
#
# 注意：每个形体的底面也需要计入表面积中。
#
#
#
#
#
#
# 示例 1：
#
#
# 输入：grid = [[1,2],[3,4]]
# 输出：34
#
#
# 示例 2：
#
#
# 输入：grid = [[1,1,1],[1,0,1],[1,1,1]]
# 输出：32
#
#
# 示例 3：
#
#
# 输入：grid = [[2,2,2],[2,1,2],[2,2,2]]
# 输出：46
#
#
#
#
# 提示：
#
#
# n == grid.length
# n == grid[i].length
# 1 <= n <= 50
# 0 <= grid[i][j] <= 50
#
#
#

from comm import *
# @lc code=start
class Solution:
    def surfaceArea(self, grid: List[List[int]]) -> int:
        """暴力法
        按层次计算每个块对面积的贡献度
        """
        self.res = 0
        def is_marked(x, y):
            if x < 0 or x >= grid_size:
                return False
            if y < 0 or y >= grid_size:
                return False
            return marked[x][y]

        def count_one_block(x, y, level=0):
            if level == 0:   # 第一层的顶部面积就是整体的顶部面积,
                self.res += 2   # 顶和底的面积相等
            if not is_marked(x-1, y):  # 如果该方向上没有其他块, 贡献1, 否则-1
                self.res += 1
            else:
                self.res -= 1
            if not is_marked(x+1, y):
                self.res += 1
            else:
                self.res -= 1
            if not is_marked(x, y-1):
                self.res += 1
            else:
                self.res -= 1
            if not is_marked(x, y+1):
                self.res += 1
            else:
                self.res -= 1
            marked[x][y] = True

        grid_size = len(grid)
        max_n = max([i for row in grid for i in row])
        for level in range(max_n):
            marked = [[False for _ in range(grid_size)] for i in range(grid_size)]
            for x in range(len(grid)):
                for y in range(len(grid[x])):
                    if grid[x][y] <= 0:
                        continue
                    count_one_block(x, y, level)
                    grid[x][y] -= 1

        return self.res

class WrongSolution:
    def surfaceArea(self, grid: List[List[int]]) -> int:
        """3视图法, 有bug无法解决向内凹的情况"""

        X = len(grid)
        Y = len(grid[0])
        ans = X * Y    # 俯视图
        x_maxes = [0] * X
        y_maxes = [0] * Y
        for x in range(X):
            for y in range(Y):
                x_maxes[x] = max(x_maxes[x], grid[x][y])   # 正视图
                y_maxes[y] = max(y_maxes[y], grid[x][y])  # 左视图
        return (ans + sum(x_maxes) + sum(y_maxes)) * 2   # 加上对面的面积
# @lc code=end

s = Solution().surfaceArea([[2]])
print(s)
s = Solution().surfaceArea([[1,2],[3,4]])
print(s)
