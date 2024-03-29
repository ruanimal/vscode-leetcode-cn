#
# @lc app=leetcode.cn id=840 lang=python3
#
# [840] 矩阵中的幻方
#
# https://leetcode-cn.com/problems/magic-squares-in-grid/description/
#
# algorithms
# Medium (36.22%)
# Likes:    57
# Dislikes: 0
# Total Accepted:    9.9K
# Total Submissions: 27.1K
# Testcase Example:  '[[4,3,8,4],[9,5,1,9],[2,7,6,2]]'
#
# 3 x 3 的幻方是一个填充有 从 1 到 9  的不同数字的 3 x 3 矩阵，其中每行，每列以及两条对角线上的各数之和都相等。
#
# 给定一个由整数组成的row x col 的 grid，其中有多少个 3 × 3 的 “幻方” 子矩阵？（每个子矩阵都是连续的）。
#
#
#
# 示例 1：
#
#
#
#
# 输入: grid = [[4,3,8,4],[9,5,1,9],[2,7,6,2]
# 输出: 1
# 解释:
# 下面的子矩阵是一个 3 x 3 的幻方：
#
# 而这一个不是：
#
# 总的来说，在本示例所给定的矩阵中只有一个 3 x 3 的幻方子矩阵。
#
#
# 示例 2:
#
#
# 输出: grid = [[8]]
# 输入: 0
#
#
#
#
# 提示:
#
#
# row == grid.length
# col == grid[i].length
# 1 <= row, col <= 10
# 0 <= grid[i][j] <= 15
#
#
#

from comm import *
# @lc code=start
class Solution(object):
    def numMagicSquaresInside(self, grid: List[List[int]]) -> int:
        """暴力法 + 集合
        """

        all_ok = {
            tuple([8,1,6,3,5,7,4,9,2]),
            tuple([6,1,8,7,5,3,2,9,4]),
            tuple([4,9,2,3,5,7,8,1,6]),
            tuple([2,9,4,7,5,3,6,1,8]),
            tuple([6,7,2,1,5,9,8,3,4]),
            tuple([8,3,4,1,5,9,6,7,2]),
            tuple([2,7,6,9,5,1,4,3,8]),
            tuple([4,3,8,9,5,1,2,7,6]),
        }

        if not grid:
            return

        ans = 0
        x, y = len(grid), len(grid[0])
        if x < 3 or y < 3:
            return 0
        for i in range(1, x-1):
            for j in range(1, y-1):
                if (
                    grid[i-1][j-1], grid[i-1][j], grid[i-1][j+1],
                    grid[ i ][j-1], grid[ i ][j], grid[ i ][j+1],
                    grid[i+1][j-1], grid[i+1][j], grid[i+1][j+1],
                ) in all_ok:
                    ans += 1
        return ans

# @lc code=end
if __name__ == "__main__":
    s = Solution().numMagicSquaresInside([[4,3,8,4], [9,5,1,9], [2,7,6,2]])
    print(s)
