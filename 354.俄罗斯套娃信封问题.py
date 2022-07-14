#
# @lc app=leetcode.cn id=354 lang=python3
#
# [354] 俄罗斯套娃信封问题
#
# https://leetcode-cn.com/problems/russian-doll-envelopes/description/
#
# algorithms
# Hard (44.38%)
# Likes:    685
# Dislikes: 0
# Total Accepted:    80.6K
# Total Submissions: 183.7K
# Testcase Example:  '[[5,4],[6,4],[6,7],[2,3]]'
#
# 给你一个二维整数数组 envelopes ，其中 envelopes[i] = [wi, hi] ，表示第 i 个信封的宽度和高度。
#
# 当另一个信封的宽度和高度都比这个信封大的时候，这个信封就可以放进另一个信封里，如同俄罗斯套娃一样。
#
# 请计算 最多能有多少个 信封能组成一组“俄罗斯套娃”信封（即可以把一个信封放到另一个信封里面）。
#
# 注意：不允许旋转信封。
#
#
# 示例 1：
#
#
# 输入：envelopes = [[5,4],[6,4],[6,7],[2,3]]
# 输出：3
# 解释：最多信封的个数为 3, 组合为: [2,3] => [5,4] => [6,7]。
#
# 示例 2：
#
#
# 输入：envelopes = [[1,1],[1,1],[1,1]]
# 输出：1
#
#
#
#
# 提示：
#
#
# 1 <= envelopes.length <= 10^5
# envelopes[i].length == 2
# 1 <= wi, hi <= 10^5
#
#
#
from comm import *

# @lc code=start

from itertools import groupby

class Solution_A:
    def maxEnvelopes(self, envelopes: List[List[int]]) -> int:
        """
        二阶动态规划, 超时
        """



        if len(envelopes) == 0:
            return 0

        envelopes.sort()
        envelopes = [list(itmes) for _, itmes in groupby(envelopes, key=lambda i: i[0])]
        dp = [[1] * len(i) for i in envelopes]
        for x in range(len(envelopes)):
            for y in range(len(envelopes[x])):
                for i in range(x):
                    for j in range(len(envelopes[i])-1, -1, -1):
                        # envelopes[x][y][0] > envelopes[i][j][0] 一定
                        if envelopes[x][y][1] > envelopes[i][j][1]:  #  envelopes[x][y][1] > envelopes[i][j][1]
                            dp[x][y] = max(dp[x][y], dp[i][j]+1)
                            break
        return max(max(i) for i in dp)

class SolutionA:
    def maxEnvelopes(self, envelopes: List[List[int]]) -> int:
        """
        二阶动态规划, 加二分查找, 超时
        """

        if len(envelopes) == 0:
            return 0

        envelopes.sort()
        envelopes = [list(itmes) for _, itmes in groupby(envelopes, key=lambda i: i[0])]
        dp = [[1] * len(i) for i in envelopes]
        for x in range(len(envelopes)):
            for y in range(len(envelopes[x])):
                for i in range(x):
                    j = self.binary_search(envelopes[i], envelopes[x][y][1])
                    if j >= 0:
                        dp[x][y] = max(dp[x][y], dp[i][j]+1)
        return max(max(i) for i in dp)

    @staticmethod
    def binary_search(nums, target):
        """
        寻找小于target的最大数
        """

        if not nums:
            return -1

        left = 0
        right = len(nums) - 1

        while left < right:
            mid = (left + right) >> 1
            if nums[mid][1] < target:
                left = mid + 1  # nums[left]为第一个大于等于target的数
            else:
                right = mid
        # print('=', left, right)
        if nums[left][1] < target:
            return left
        return left - 1

class Solution:
    def maxEnvelopes(self, envelopes: List[List[int]]) -> int:
        """
        一阶动态规划, 加二分查找
        """

        if len(envelopes) == 0:
            return 0

        nums = [i[1] for i in sorted(envelopes, key=lambda i: (i[0], -i[1]))]
        # print(nums)
        top = []
        for i in nums:
            pos = self.find_first(top, i)
            if pos == -1:
                top.append(i)
            else:
                top[pos] = i
        # print(top)
        return len(top)

    @staticmethod
    def find_first(nums: List[int], target: int) -> int:
        if len(nums) == 0:
            return -1
        left = 0
        right = len(nums)-1
        while left <= right:
            mid = (left+right) >> 1
            if nums[mid] < target:
                left = mid + 1
            else:
                right = mid - 1
        # print(nums, target, left)
        if left == len(nums):
            return -1
        return left
# @lc code=end


s = Solution()
# data = [[1,15],[7,18],[7,6],[7,100],[2,200],[17,30],[17,45],[3,5],[7,8],[3,6],[3,10],[7,20],[17,3],[17,45]]
data = [[1,3],[3,5],[6,7],[6,8],[8,4],[9,5]]
print(s.maxEnvelopes(data))
# print(s.maxEnvelopes([[5,4],[6,4],[6,7],[2,3]]))
# print(sorted(data))

# print(s.binary_search([[0, 1], [0, 2], [0, 2], [0, 7]], 2))
# print(s.binary_search([[0, 1], [0, 2], [0, 7]], 3))
# print(s.binary_search([[0, 1], [0, 2], [0, 7]], 9))
# print(s.binary_search([[0, 1], [0, 2], [0, 7]], 0))
