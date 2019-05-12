#
# @lc app=leetcode.cn id=1030 lang=python
#
# [1030] 距离顺序排列矩阵单元格
#
class Solution(object):
    def allCellsDistOrder(self, R, C, r0, c0):
        """
        :type R: int
        :type C: int
        :type r0: int
        :type c0: int
        :rtype: List[List[int]]
        """
        dis_map = {}
        for x in range(0, R):
            for y in range(0, C):
                dis_map[(x, y)] = abs(x-r0) + abs(y-c0)
        return [list(i[0]) for i in sorted(dis_map.items(), key=lambda i: i[1])]

if __name__ == "__main__":
    s = Solution().allCellsDistOrder(R = 1, C = 2, r0 = 0, c0 = 0)
    print(s)
    s = Solution().allCellsDistOrder(R = 2, C = 2, r0 = 0, c0 = 1)
    print(s)
    s = Solution().allCellsDistOrder(R = 3, C = 5, r0 = 2, c0 = 3)
    print(s)


