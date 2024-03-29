#
# @lc app=leetcode.cn id=941 lang=python3
#
# [941] 有效的山脉数组
#
# https://leetcode-cn.com/problems/valid-mountain-array/description/
#
# algorithms
# Easy (33.00%)
# Likes:    18
# Dislikes: 0
# Total Accepted:    3.3K
# Total Submissions: 9.7K
# Testcase Example:  '[2,1]'
#
# 给定一个整数数组 A，如果它是有效的山脉数组就返回 true，否则返回 false。
#
# 让我们回顾一下，如果 A 满足下述条件，那么它是一个山脉数组：
#
#
# A.length >= 3
# 在 0 < i < A.length - 1 条件下，存在 i 使得：
#
# A[0] < A[1] < ... A[i-1] < A[i]
# A[i] > A[i+1] > ... > A[B.length - 1]
#
#
#
#
#
#
# 示例 1：
#
# 输入：[2,1]
# 输出：false
#
#
# 示例 2：
#
# 输入：[3,5,5]
# 输出：false
#
#
# 示例 3：
#
# 输入：[0,3,2,1]
# 输出：true
#
#
#
# 提示：
#
#
# 0 <= A.length <= 10000
# 0 <= A[i] <= 10000 
#
#
#
#
#
#
#

from comm import *
# @lc code=start
class Solution:
    def validMountainArray(self, A: List[int]):
        """暴力法
        可用二分查找
        """

        if len(A) < 3:
            return False
        peak_cnt = 0
        for i in range(1, len(A)-1):
            if A[i-1] < A[i] and A[i] > A[i+1]:   # peak
                peak_cnt += 1
            elif A[i-1] < A[i] < A[i+1] or A[i-1] > A[i] > A[i+1]:   # left side or right side
                continue
            else:
                return False
        return peak_cnt == 1

# @lc code=end
if __name__ == "__main__":
    s = Solution().validMountainArray([0,3,2,1])
    print(s)
    s = Solution().validMountainArray([1,1,1])
    print(s)
    s = Solution().validMountainArray([1,2,1])
    print(s)
    s = Solution().validMountainArray([1,2,1,1,1])
    print(s)
    s = Solution().validMountainArray([0,1,2,1,2])
    print(s)
    s = Solution().validMountainArray([14,82,89,84,79,70,70,68,67,66,63,60,58,54,44,43,32,28,26,25,22,15,13,12,10,8,7,5,4,3])
    print(s)

