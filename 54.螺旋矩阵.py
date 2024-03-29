#
# @lc app=leetcode.cn id=54 lang=python3
#
# [54] 螺旋矩阵
#
# https://leetcode-cn.com/problems/spiral-matrix/description/
#
# algorithms
# Medium (35.02%)
# Likes:    167
# Dislikes: 0
# Total Accepted:    16.2K
# Total Submissions: 44.8K
# Testcase Example:  '[[1,2,3],[4,5,6],[7,8,9]]'
#
# 给定一个包含 m x n 个元素的矩阵（m 行, n 列），请按照顺时针螺旋顺序，返回矩阵中的所有元素。
#
# 示例 1:
#
# 输入:
# [
# ⁠[ 1, 2, 3 ],
# ⁠[ 4, 5, 6 ],
# ⁠[ 7, 8, 9 ]
# ]
# 输出: [1,2,3,6,9,8,7,4,5]
#
#
# 示例 2:
#
# 输入:
# [
# ⁠ [1, 2, 3, 4],
# ⁠ [5, 6, 7, 8],
# ⁠ [9,10,11,12]
# ]
# 输出: [1,2,3,4,8,12,11,10,9,5,6,7]
#
#
#
class Solution(object):
    def spiralOrder(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: List[int]
        """
        if len(matrix) <= 1:
            return sum(matrix, [])

        m = len(matrix)
        n = len(matrix[0])
        ans = []
        pos = [0, -1]
        # 前进方向, 通过(坐标轴, 移动量)表示
        heads = [
            (1, 1),  # y轴, 往下移动1
            (0, 1),  # x轴, 往右移动1
            (1, -1),
            (0, -1),
        ]
        head = heads[0]
        next_head = lambda h: heads[(heads.index(h)+1) % 4]
        for i in range(1, m * n + 1):
            pos[head[0]] += head[1]
            # 一个方向越界了或者该位置已经走过, 说明需要换方向
            if pos[0] >= m or pos[1] >= n or pos[0] < 0 or pos[1] < 0 or matrix[pos[0]][pos[1]] is None:
                pos[head[0]] -= head[1]
                head = next_head(head)
                pos[head[0]] += head[1]
            ans.append(matrix[pos[0]][pos[1]])
            matrix[pos[0]][pos[1]] = None
        return ans

if __name__ == "__main__":
    s = Solution().spiralOrder([
        [ 1, 2, 3 ],
        [ 4, 5, 6 ],
        [ 7, 8, 9 ]
        ])
    print(s)
    s = Solution().spiralOrder([
            [3],
            [2]
        ])
    print(s)
    s = Solution().spiralOrder([
            [1]
        ])
    print(s)
