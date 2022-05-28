#
# @lc app=leetcode.cn id=643 lang=python3
#
# [643] 子数组最大平均数 I
#
# https://leetcode-cn.com/problems/maximum-average-subarray-i/description/
#
# algorithms
# Easy (33.37%)
# Likes:    49
# Dislikes: 0
# Total Accepted:    5K
# Total Submissions: 14.4K
# Testcase Example:  '[1,12,-5,-6,50,3]\n4'
#
# 给定 n 个整数，找出平均数最大且长度为 k 的连续子数组，并输出该最大平均数。
#
# 示例 1:
#
# 输入: [1,12,-5,-6,50,3], k = 4
# 输出: 12.75
# 解释: 最大平均数 (12-5-6+50)/4 = 51/4 = 12.75
#
#
#
#
# 注意:
#
#
# 1 <= k <= n <= 30,000。
# 所给数据范围 [-10,000，10,000]。
#
#
#

from comm import *
# @lc code=start
class Solution(object):
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        """模拟队列, 用一个字段模拟队列总和, 模拟入队出队操作
        """
        if len(nums) == 0:
            return
        tmp = 0
        k = float(k)
        ans = float('-inf')
        total = 0
        for idx, i in enumerate(nums):
            if tmp < k:
                tmp += 1
                total += i
                ans = total
            else:
                total += i   # 模拟入队和出队
                total -= nums[idx-tmp]
                ans = max(ans, total)
        return ans / k

# @lc code=end

if __name__ == "__main__":
    s = Solution().findMaxAverage([1,12,-5,-6,50,3], k = 4)
    print(s)
    s = Solution().findMaxAverage([1,12,-5,-6,50,3], k = 1)
    print(s)
    s = Solution().findMaxAverage([5], k = 1)
    print(s)
    s = Solution().findMaxAverage([4,0,4,3,3], 5)
    print(s)

