#
# @lc app=leetcode.cn id=51 lang=python3
#
# [51] N皇后
#
# https://leetcode-cn.com/problems/n-queens/description/
#
# algorithms
# Hard (58.59%)
# Total Accepted:    5.5K
# Total Submissions: 9.2K
# Testcase Example:  '4'
#
# n 皇后问题研究的是如何将 n 个皇后放置在 n×n 的棋盘上，并且使皇后彼此之间不能相互攻击。
#
#
#
# 上图为 8 皇后问题的一种解法。
#
# 给定一个整数 n，返回所有不同的 n 皇后问题的解决方案。
#
# 每一种解法包含一个明确的 n 皇后问题的棋子放置方案，该方案中 'Q' 和 '.' 分别代表了皇后和空位。
#
# 示例:
#
# 输入: 4
# 输出: [
# ⁠[".Q..",  // 解法 1
# ⁠ "...Q",
# ⁠ "Q...",
# ⁠ "..Q."],
#
# ⁠["..Q.",  // 解法 2
# ⁠ "Q...",
# ⁠ "...Q",
# ⁠ ".Q.."]
# ]
# 解释: 4 皇后问题存在两个不同的解法。
#
#
#
class SolutionV1(object):
    def solveNQueens_1(self, n):
        """
        :type n: int
        :rtype: List[List[str]]

        求一种解法
        """
        def queens(board, current):
            if current == n:
                return True
            else:
                for i in range(n):
                    board[current] = i
                    if no_confict(board, current):
                        done = queens(board, current+1)
                        if done:
                            return True
                return False

        def no_confict(board, current):
            for i in range(current):
                if board[i] == board[current]:
                    return False
                if (current-i) == abs(board[i] - board[current]):
                    return False
            return True

        board = [-1] * n
        if queens(board, 0):
            return board


    def solveNQueens(self, n):
        """
        :type n: int
        :rtype: List[List[str]]
        """
        def dfs(n, pie, na, res, path):
            # 第n行, 撇, 捺, 结果,
            #终止的条件
            #res 可以把列数存下来
            row = len(path)   # 行
            if row == n:
                res.append(path)
                return

            for col in range(n):  # 列
                if (
                        col not in path and   # 竖向没被占用
                        (row-col) not in pie and  #  行减列的数值可以代表一条斜线上的位置
                        (row+col) not in na  # 另一个方向斜线
                ):
                    pie[row-col] = 1
                    na[row+col] = 1
                    dfs(n, pie, na, res, path+[col])
                    del pie[row-col]
                    del na[row+col]
        res = []
        dfs(n, {}, {}, res, [])
        return [['.'*i + 'Q' + '.'*(n-i-1) for i in sol] for sol in res]


EMPTY = '.'
QUEEN = 'Q'

class Solution(object):
    def solveNQueens(self, n):
        """
        回溯法判断矩阵的每个位置是否能够放置, 回溯每一行的每个位置
        如果这个点所在位置的横竖撇捺的方向上都可以放置, 那么该点就是可以放置的, 否则直接剪枝.
        """

        def can_put(i, j):
            return (heng.get(i, 0) == 0 and shu.get(j, 0) == 0
                    and pie.get(i+j, 0) == 0 and na.get(i-j, 0) == 0)

        def backtrack(res, i):
            if i == n:
                res.append([''.join(i) for i in board])
                return

            for j in range(n):
                if can_put(i, j):   # 剪枝: 把明显不满足的去掉
                    board[i][j] = QUEEN
                    heng[i] = 1
                    shu[j] = 1
                    pie[i+j] = 1
                    na[i-j] = 1
                    backtrack(res, i+1)
                    heng[i] = 0
                    shu[j] = 0
                    pie[i+j] = 0
                    na[i-j] = 0
                    board[i][j] = EMPTY

        if n == 1:
            return [['Q']]
        board = [['.'] * n for _ in range(n)]
        res = []
        heng = {}
        shu = {}
        pie = {}
        na = {}
        backtrack(res, 0)
        return res

if __name__ == "__main__":
    pass
    # import ipdb;ipdb.set_trace()
    print(Solution().solveNQueens(1))
    # print(Solution().solveNQueens(10))
