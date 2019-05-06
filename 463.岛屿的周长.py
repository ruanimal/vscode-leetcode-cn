#
# @lc app=leetcode.cn id=463 lang=python
#
# [463] 岛屿的周长
#
class Solution(object):
    def islandPerimeter(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """

        marks_map = []
        begin = None
        for x in range(len(grid)):
            marks_map.append([])
            for y in range(len(grid[0])):
                marks_map[x].append(False)
                if not begin and grid[x][y] == 1:
                    begin = (x, y)

        length = 0
        level = []
        marks_map[begin[0]][begin[1]] = True
        level.append(begin)
        while level:
            next_level = []
            for x, y in level:
                length += 4
                for nx, ny in [(x+1, y), (x-1, y), (x, y+1), (x, y-1),]:
                    if (0 <= nx < len(grid)) and (0 <= ny < len(grid[0])):
                        if grid[nx][ny] == 1:
                            length -= 1
                            if not marks_map[nx][ny]:
                                next_level.append((nx, ny))
                                marks_map[nx][ny] = True
            level = next_level
        return length

if __name__ == "__main__":
    s = Solution().islandPerimeter([[0,1,0,0],
        [1,1,1,0],
        [0,1,0,0],
        [1,1,0,0]])
    print(s)
    s = Solution().islandPerimeter([[1,1], [1,1]])
    print(s)
