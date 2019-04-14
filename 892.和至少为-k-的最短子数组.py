#
# @lc app=leetcode.cn id=892 lang=python
#
# [892] 和至少为 K 的最短子数组
#
# https://leetcode-cn.com/problems/surface-area-of-3d-shapes/description/
#
# algorithms
# Easy (48.26%)
# Total Accepted:    1.5K
# Total Submissions: 3K
# Testcase Example:  '[[2]]'
#
# 在 N * N 的网格上，我们放置一些 1 * 1 * 1  的立方体。
#
# 每个值 v = grid[i][j] 表示 v 个正方体叠放在单元格 (i, j) 上。
#
# 返回结果形体的总表面积。
#
#
#
#
#
#
# 示例 1：
#
# 输入：[[2]]
# 输出：10
#
#
# 示例 2：
#
# 输入：[[1,2],[3,4]]
# 输出：34
#
#
# 示例 3：
#
# 输入：[[1,0],[0,2]]
# 输出：16
#
#
# 示例 4：
#
# 输入：[[1,1,1],[1,0,1],[1,1,1]]
# 输出：32
#
#
# 示例 5：
#
# 输入：[[2,2,2],[2,1,2],[2,2,2]]
# 输出：46
#
#
#
#
# 提示：
#
#
# 1 <= N <= 50
# 0 <= grid[i][j] <= 50
#
#
#
class Solution(object):
    def surfaceArea(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
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

if __name__ == "__main__":
    # data = [[2]]
    # data = [[1,0],[0,2]]
    data = [[2,2,2],[2,1,2],[2,2,2]]
    s = Solution().surfaceArea(data)
    print(s)


