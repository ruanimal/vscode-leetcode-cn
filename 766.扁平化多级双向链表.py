#
# @lc app=leetcode.cn id=766 lang=python
#
# [766] 扁平化多级双向链表
#
class Solution(object):
    def isToeplitzMatrix(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: bool
        """
        ans = []
        for x in range(len(matrix)):
            tmp = set()
            y = 0
            while x < len(matrix) and y < len(matrix[0]):
                tmp.add(matrix[x][y])
                x += 1
                y += 1
                if len(tmp) != 1:
                    return False
            ans.append(tmp)
        for y in range(len(matrix[0])):
            tmp = set()
            x = 0
            while x < len(matrix) and y < len(matrix[0]):
                tmp.add(matrix[x][y])
                x += 1
                y += 1
                if len(tmp) != 1:
                    return False
            ans.append(tmp)
        return True

if __name__ == "__main__":
    s = Solution().isToeplitzMatrix([
        [1,2,3,4],
        [5,1,2,3],
        [9,5,1,2]
    ])
    print(s)
