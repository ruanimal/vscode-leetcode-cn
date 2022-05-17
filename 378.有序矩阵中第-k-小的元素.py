#
# @lc app=leetcode.cn id=378 lang=python3
#
# [378] 有序矩阵中第 K 小的元素
#
# https://leetcode-cn.com/problems/kth-smallest-element-in-a-sorted-matrix/description/
#
# algorithms
# Medium (63.16%)
# Likes:    791
# Dislikes: 0
# Total Accepted:    97.8K
# Total Submissions: 154.7K
# Testcase Example:  '[[1,5,9],[10,11,13],[12,13,15]]\n8'
#
# 给你一个 n x n 矩阵 matrix ，其中每行和每列元素均按升序排序，找到矩阵中第 k 小的元素。
# 请注意，它是 排序后 的第 k 小元素，而不是第 k 个 不同 的元素。
#
# 你必须找到一个内存复杂度优于 O(n^2) 的解决方案。
#
#
#
# 示例 1：
#
#
# 输入：matrix = [[1,5,9],[10,11,13],[12,13,15]], k = 8
# 输出：13
# 解释：矩阵中的元素为 [1,5,9,10,11,12,13,13,15]，第 8 小元素是 13
#
#
# 示例 2：
#
#
# 输入：matrix = [[-5]], k = 1
# 输出：-5
#
#
#
#
# 提示：
#
#
# n == matrix.length
# n == matrix[i].length
# 1 <= n <= 300
# -10^9 <= matrix[i][j] <= 10^9
# 题目数据 保证 matrix 中的所有行和列都按 非递减顺序 排列
# 1 <= k <= n^2
#
#
#
#
# 进阶：
#
#
# 你能否用一个恒定的内存(即 O(1) 内存复杂度)来解决这个问题?
# 你能在 O(n) 的时间复杂度下解决这个问题吗?这个方法对于面试来说可能太超前了，但是你会发现阅读这篇文章（ this paper ）很有趣。
#
#
#

from comm import *
# @lc code=start

from queue import PriorityQueue

class SolutionA:
    def kthSmallest(self, matrix: List[List[int]], k: int) -> int:
        """
        使用最小堆(优先队列)
        """

        length = len(matrix)
        pq = PriorityQueue()
        for idx, i in enumerate(matrix):
            pq.put((i[0], idx, 0))
        i = j = 0
        while not pq.empty() and k > 0:
            val, i, j = pq.get()
            k -= 1
            if j+1 < length:
                pq.put((matrix[i][j+1], i, j+1))
        return matrix[i][j]


class Solution:
    def kthSmallest(self, matrix: List[List[int]], k: int) -> int:
        """二分查找
        在矩阵的最大值和最小值的区间中, 寻找一个数字, 使得小于等于该值的数字个数等于k
        由于数字不是连续的, 会有多个值满足, 取最小那个.

        也就把问题转化为, 二分查找包含相同元素的情况, 取第一个元素
        """
        left = matrix[0][0]
        right = matrix[-1][-1]
        while left <= right:
            mid = (left + right) >> 1
            if self.search(matrix, mid) >= k:
                right = mid - 1
            else:
                left = mid + 1
        return left

    def search(self, matrix: List[List[int]], target: int) -> int:
        """查找二维矩阵中, 小于等于target的元素个数"""

        M = len(matrix)
        N = len(matrix[0])
        i, j = 0, N-1
        nums = 0
        while i < M and j >= 0:
            # print(i, j)
            if matrix[i][j] > target:
                j -= 1
            else:
                i += 1
                nums += (j+1)
        return nums

# @lc code=end

s = Solution().kthSmallest([[1,5,9],
                      [10,11,13],
                      [12,13,15]], 2)
print(s)
