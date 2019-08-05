class Solution:
    def largest1BorderedSquare(self, grid):
        if not grid:
            return 0
        max_width = 0
        max_x = len(grid)
        max_y = len(grid[0])
        for i in range(max_x):
            for j in range(max_y):
                if (max_x-i>max_width) and (max_y-j>max_y):
                    max_width = max(max_width, self.search_one(grid, (i, j)))
        return max_width ** 2

    @staticmethod
    def search_one(grid, pos):
        max_x = len(grid)
        max_y = len(grid[0])
        x, y = pos
        width = min((max_x-x), (max_y-y))
        ans = 0
        for i in range(width):
            if not grid[x+i] or not grid[x][y+i]:
                ans = i
                break
            if any(not grid[i][y + j] for j in range(i)) or any(not grid[x + j][y] for j in range(i)):
                continue
        return ans


if __name__ == "__main__":
    s = Solution().largest1BorderedSquare(
        [[1, 1, 1], [1, 0, 1], [1, 1, 1]]
    )
    print(s)
