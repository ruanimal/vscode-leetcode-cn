#
# @lc app=leetcode.cn id=447 lang=python
#
# [447] 回旋镖的数量
#
class Solution(object):
    def numberOfBoomerangs(self, points):
        """
        :type points: List[List[int]]
        :rtype: int
        """
        import itertools

        ans = 0
        counts_map = {}
        for i in points:
            for j in points:
                x1, y1 = i
                x2, y2 = j
                dis = (x1-x2)**2 + (y1-y2)**2
                counts_map[dis] = counts_map.get(dis, 0) + 1
            for dis, count in counts_map.items():
                ans += count*(count-1)   # 该距离的点有count个, 可组成count*(count-1)个回旋镖
            counts_map = {}
        return ans
if __name__ == "__main__":
    s = Solution().numberOfBoomerangs([[0,0],[1,0],[2,0]])
    print(s)

