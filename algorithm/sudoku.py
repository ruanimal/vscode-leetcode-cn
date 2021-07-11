from copy import deepcopy
import time

board = [
    [0, 0, 9, 8, 2, 6, 7, 4, 5],
    [7, 2, 0, 0, 9, 0, 6, 0, 0],
    [5, 8, 6, 4, 3, 0, 0, 2, 0],
    [6, 0, 0, 0, 0, 4, 0, 0, 0],
    [0, 7, 0, 6, 0, 9, 8, 1, 0],
    [4, 9, 8, 3, 0, 0, 5, 6, 7],
    [0, 4, 0, 5, 0, 1, 0, 0, 9],
    [9, 6, 0, 0, 4, 0, 1, 5, 0],
    [0, 0, 5, 0, 7, 3, 0, 8, 6],
]

board = [
    [0, 8, 6, 9, 0, 2, 0, 0, 0],
    [0, 0, 7, 0, 0, 0, 0, 0, 0],
    [5, 2, 0, 0, 0, 7, 0, 0, 0],
    [2, 0, 0, 0, 0, 0, 0, 0, 6],
    [0, 0, 5, 0, 0, 0, 0, 0, 0],
    [0, 3, 1, 0, 0, 6, 0, 8, 2],
    [0, 0, 0, 4, 0, 9, 6, 5, 0],
    [0, 0, 0, 0, 1, 0, 2, 0, 3],
    [4, 1, 0, 6, 0, 5, 0, 0, 0],
]

# board = [
#     [1, 2, 3, 4, 5, 6, 7, 8, 9],
#     [4, 5, 6, 7, 8, 9, 1, 2, 3],
#     [7, 8, 9, 1, 2, 3, 4, 5, 6],
#     [2, 3, 4, 5, 6, 7, 8, 9, 1],
#     [5, 6, 7, 8, 9, 1, 2, 3, 4],
#     [8, 9, 1, 2, 3, 4, 5, 6, 7],
#     [3, 4, 5, 0, 0, 0, 0, 0, 0],
#     [0, 0, 0, 0, 0, 0, 0, 0, 0],
#     [0, 0, 0, 0, 0, 0, 0, 0, 0],
# ]

TMP = '''\
{} {} {} | {} {} {} | {} {} {}
{} {} {} | {} {} {} | {} {} {}
{} {} {} | {} {} {} | {} {} {}
---------------------
{} {} {} | {} {} {} | {} {} {}
{} {} {} | {} {} {} | {} {} {}
{} {} {} | {} {} {} | {} {} {}
---------------------
{} {} {} | {} {} {} | {} {} {}
{} {} {} | {} {} {} | {} {} {}
{} {} {} | {} {} {} | {} {} {}
=====================
'''

EMPTY = 0

def print_board(board):
    print(TMP.format(*sum(board, [])))


# print_board(board)

def is_valid(board):
    # init data
    rows = [{} for i in range(9)]
    columns = [{} for i in range(9)]
    boxes = [{} for i in range(9)]

    # validate a board
    for i in range(9):
        for j in range(9):
            num = board[i][j]
            if num != EMPTY:
                num = int(num)
                box_index = (i // 3 ) * 3 + j // 3

                # keep the current cell value
                rows[i][num] = rows[i].get(num, 0) + 1
                columns[j][num] = columns[j].get(num, 0) + 1
                boxes[box_index][num] = boxes[box_index].get(num, 0) + 1

                # check if this value has been already seen before
                if rows[i][num] > 1 or columns[j][num] > 1 or boxes[box_index][num] > 1:
                    return False
    return True

# print(is_valid(board))

res = set()
step = 0

def brute_force(board):
    def can_put(board, row, col, c):
        # print(row, col, c)
        for i in range(9):
            if board[i][col] != EMPTY and board[i][col] == c:
                return False
            if board[row][i] != EMPTY and board[row][i] == c:
                return False
            x, y = row // 3 * 3 + i // 3,  col // 3 * 3 + i % 3
            if board[x][y] != EMPTY and board[x][y] == c:
                return False
        # print(row, col, c, True)
        return True

    def solve(board):
        global step
        for i in range(9):
            for j in range(9):
                if board[i][j] == EMPTY:
                    for c in range(1, 10):
                        step += 1
                        if can_put(board, i, j, c):
                            board[i][j] = c
                            if solve(board):
                                return True
                            else:
                                board[i][j] = EMPTY
                    return False
        print_board(board)
        return True

    if not is_valid(board):
        return False
    return solve(board)

# start = time.time()
# step = 0
# print(brute_force(deepcopy(board)))
# print(step, time.time() - start)


def brute_force_v2(board):
    def solve(board):
        global step
        for i in range(9):
            for j in range(9):
                box_index = (i // 3 ) * 3 + j // 3
                if board[i][j] == EMPTY:
                    for c in (rows[i] & columns[j] & boxes[box_index]):    # 通过集合来剪枝
                        step += 1
                        # 设置状态
                        board[i][j] = c
                        tmp = [False, False, False]
                        for idx, elem in enumerate((rows[i], columns[j], boxes[box_index])):
                            if c in elem:
                                elem.remove(c)
                                tmp[idx] = True
                        # 进入下一层递归
                        if solve(board):
                            return True
                        # 还原状态
                        board[i][j] = EMPTY
                        for idx, elem in zip(tmp, (rows[i], columns[j], boxes[box_index])):
                            if idx:
                                elem.add(c)
                    return False
        print_board(board)
        return True

    # 验证题目是否合法, 初始化每一格可选择项
    rows = [set(range(1,10)) for i in range(9)]
    columns = [set(range(1,10)) for i in range(9)]
    boxes = [set(range(1,10)) for i in range(9)]
    for i in range(9):
        for j in range(9):
            num = board[i][j]
            if num != EMPTY:
                num = int(num)
                box_index = (i // 3 ) * 3 + j // 3
                if num not in rows[i]:
                    return False
                rows[i].remove(num)
                if num not in columns[j]:
                    return False
                columns[j].remove(num)
                if num not in boxes[box_index]:
                    return False
                boxes[box_index].remove(num)
    return solve(board)

start = time.time()
step = 0
print(brute_force_v2(deepcopy(board)))
print(step)
print(step, time.time() - start)

# 这是错的, 不能只回溯剩下的位置, 因为当前位置的选择会影响别的位置
def brute_force_v3(board):
    def solve(board, start_i=0, start_j=0):
        global step
        for i in range(start_i, 9):
            for j in range(start_j, 9):
                box_index = (i // 3 ) * 3 + j // 3
                if board[i][j] == EMPTY:
                    for c in (rows[i] & columns[j] & boxes[box_index]):    # 通过集合来剪枝
                        step += 1
                        # 设置状态
                        board[i][j] = c
                        tmp = [False, False, False]
                        for idx, elem in enumerate((rows[i], columns[j], boxes[box_index])):
                            if c in elem:
                                elem.remove(c)
                                tmp[idx] = True
                        # 进入下一层递归
                        res = solve(board, i, j+1)
                        if res:  # 满足条件终止递归分支
                            return True
                        # 还原状态
                        board[i][j] = EMPTY
                        for idx, elem in zip(tmp, (rows[i], columns[j], boxes[box_index])):
                            if idx:
                                elem.add(c)
                    return False
        print_board(board)
        return True

    # 验证题目是否合法, 初始化每一格可选择项
    rows = [set(range(1,10)) for i in range(9)]
    columns = [set(range(1,10)) for i in range(9)]
    boxes = [set(range(1,10)) for i in range(9)]
    for i in range(9):
        for j in range(9):
            num = board[i][j]
            if num != EMPTY:
                num = int(num)
                box_index = (i // 3 ) * 3 + j // 3
                if num not in rows[i]:
                    return False
                rows[i].remove(num)
                if num not in columns[j]:
                    return False
                columns[j].remove(num)
                if num not in boxes[box_index]:
                    return False
                boxes[box_index].remove(num)
    return solve(board)

# start = time.time()
# step = 0
# print(brute_force_v3(deepcopy(board)))
# print(step)
# print(step, time.time() - start)
