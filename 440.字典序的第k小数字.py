#
# @lc app=leetcode.cn id=440 lang=python
#
# [440] 字典序的第K小数字
#
# https://leetcode-cn.com/problems/k-th-smallest-in-lexicographical-order/description/
#
# algorithms
# Hard (26.45%)
# Likes:    21
# Dislikes: 0
# Total Accepted:    532
# Total Submissions: 1.9K
# Testcase Example:  '13\n2'
#
# 给定整数 n 和 k，找到 1 到 n 中字典序第 k 小的数字。
#
# 注意：1 ≤ k ≤ n ≤ 10^9。
#
# 示例 :
#
#
# 输入:
# n: 13   k: 2
#
# 输出:
# 10
#
# 解释:
# 字典序的排列是 [1, 10, 11, 12, 13, 2, 3, 4, 5, 6, 7, 8, 9]，所以第二小的数字是 10。
#
#
#

# https://leetcode.com/problems/k-th-smallest-in-lexicographical-order/discuss/92242/ConciseEasy-to-understand-Java-5ms-solution-with-Explaination
class Solution(object):
    def findKthNumber(self, n, k):
        """
        :type n: int
        :type k: int
        :rtype: int
        """
        def calSteps(n, n1, n2):
            steps = 0
            while (n1 <= n):
                steps += min(n + 1, n2) - n1
                n1 *= 10
                n2 *= 10
            return steps

        curr = 1
        k = k - 1
        while (k > 0):
            steps = calSteps(n, curr, curr + 1)
            if (steps <= k):
                curr += 1
                k -= steps
            else:
                curr *= 10
                k -= 1
        return curr

if __name__ == "__main__":
    s = Solution().findKthNumber(1000, 5)
    print(s)
