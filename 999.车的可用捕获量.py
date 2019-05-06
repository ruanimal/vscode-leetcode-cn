#
# @lc app=leetcode.cn id=999 lang=python
#
# [999] 车的可用捕获量
#
class Solution(object):
    def numRookCaptures(self, board):
        """
        :type board: List[List[str]]
        :rtype: int
        """

        '''
        # 广度优先检索, 求所有能走到的方格, 与题意不符
        marks_map = []
        rook = None
        total_pawn_count = 0
        for x in range(len(board)):
            marks_map.append([])
            for y in range(len(board[0])):
                if board[x][y] == 'B':
                    marks_map[x].append(True)
                elif board[x][y] == 'R':
                    rook = (x, y)
                    marks_map[x].append(True)
                elif board[x][y] == 'p':
                    total_pawn_count += 1
                    marks_map[x].append(False)
                else:
                    marks_map[x].append(False)

        level = []
        marks_map[rook[0]][rook[1]] = True
        level.append(rook)
        pawn_count = 0
        while level:
            next_level = []
            for x, y in level:
                if board[x][y] == 'p':
                    pawn_count += 1
                marks_map[x][y] = True
                for nx, ny in [ (x+1, y), (x-1, y), (x, y+1), (x, y-1),]:
                    if ( (0 <= nx < len(board)) and (0 <= ny < len(board[0])) and not marks_map[nx][ny]):
                        next_level.append((nx, ny))
            level = next_level
        return pawn_count
        '''

        rook = None
        for x in range(len(board)):
            for y in range(len(board[0])):
                if board[x][y] == 'R':
                    rook = (x, y)
        ret = 0
        for x in range(rook[0]+1, len(board)):
            y = rook[1]
            if board[x][y] == 'p':
                ret += 1
                break
            if board[x][y] == 'B':
                break
        for x in range(rook[0]-1, -1, -1):
            y = rook[1]
            if board[x][y] == 'p':
                ret += 1
                break
            if board[x][y] == 'B':
                break
        for y in range(rook[1]+1, len(board[0])):
            x = rook[0]
            if board[x][y] == 'p':
                ret += 1
                break
            if board[x][y] == 'B':
                break
        for y in range(rook[1]-1, -1, -1):
            x = rook[0]
            if board[x][y] == 'p':
                ret += 1
                break
            if board[x][y] == 'B':
                break
        return ret

if __name__ == "__main__":
    s = Solution().numRookCaptures([[".",".",".",".",".",".",".","."],[".",".",".","p",".",".",".","."],[".",".",".","p",".",".",".","."],["p","p",".","R",".","p","B","."],[".",".",".",".",".",".",".","."],[".",".",".","B",".",".",".","."],[".",".",".","p",".",".",".","."],[".",".",".",".",".",".",".","."]])
    print(s)

