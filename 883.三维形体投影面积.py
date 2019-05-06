#
# @lc app=leetcode.cn id=883 lang=python
#
# [883] 三维形体投影面积
#
class Solution(object):
    def projectionArea(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        ret = 0
        for x in range(len(grid)):
            ret += max(grid[x])  # y 方向投影

        for y in range(len(grid[0])):
            tmp = 0
            for x in range(len(grid)):
                if grid[x][y] > 0:
                    ret += 1  # z 方向投影
                tmp = max(tmp, grid[x][y])
            ret += tmp  # x 方向投影
        return ret

if __name__ == "__main__":
    s = Solution().projectionArea([[1,2],[3,4]])
    print(s)
