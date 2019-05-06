#
# @lc app=leetcode.cn id=575 lang=python
#
# [575] 分糖果
#
class Solution(object):
    def distributeCandies(self, candies):
        """
        :type candies: List[int]
        :rtype: int
        """
        uniq_count = len(set(candies))
        if uniq_count >= len(candies) // 2:
            return len(candies) // 2
        return uniq_count

if __name__ == "__main__":
    s = Solution().distributeCandies([1,1,2,2,3,3])
    print(s)
    s = Solution().distributeCandies([1,1,2,3])
    print(s)
