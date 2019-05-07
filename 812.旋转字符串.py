#
# @lc app=leetcode.cn id=812 lang=python
#
# [812] 旋转字符串
#
class Solution(object):
    def largestTriangleArea(self, points):
        """
        :type points: List[List[int]]
        :rtype: float
        S=(x1y2 + x2y3 + x3y1- x1y3 - x2y1 - x3y2) /2;
        """
        # 求全组合
        import itertools

        ans = 0
        for (x1, y1), (x2, y2), (x3, y3) in itertools.combinations(points, 3):
            tmp = abs((x1*y2 + x2*y3 + x3*y1 - x1*y3 - x2*y1 - x3*y2) / 2.0)
            ans = max(tmp, ans)
        return ans

if __name__ == "__main__":
    s = Solution().largestTriangleArea([[0,0],[0,1],[1,0],[0,2],[2,0]])
    print(s)
