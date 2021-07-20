#
# @lc app=leetcode.cn id=77 lang=python
#
# [77] 组合
#
# https://leetcode-cn.com/problems/combinations/description/
#
# algorithms
# Medium (76.92%)
# Likes:    625
# Dislikes: 0
# Total Accepted:    184.1K
# Total Submissions: 239.2K
# Testcase Example:  '4\n2'
#
# 给定两个整数 n 和 k，返回 1 ... n 中所有可能的 k 个数的组合。
#
# 示例:
#
# 输入: n = 4, k = 2
# 输出:
# [
# ⁠ [2,4],
# ⁠ [3,4],
# ⁠ [2,3],
# ⁠ [1,2],
# ⁠ [1,3],
# ⁠ [1,4],
# ]
#
#

class SolutionV1(object):
    def combine(self, n, k):
        """
        :type n: int
        :type k: int
        :rtype: List[List[int]]
        """

        def backtrack(start, k, res, path):
            if k == 0:
                res.append(path[:])
                return
            for i in range(start, n+1):
                # 组合的话, 为了防止重复, 已遍历的数字不要重新遍历
                if (not path or path[-1] < i):
                    path.append(i)
                    backtrack(start+1, k-1, res, path)
                    path.pop()

        if (n < k) or n == 0 or k == 0:
            return []
        res = []
        backtrack(1, k, res, [])
        return res


# @lc code=start
class Solution(object):
    def combine(self, n, k):
        """
        :type n: int
        :type k: int
        :rtype: List[List[int]]
        """

        def backtrack(start, k, res, path):
            if k == 0:
                res.append(path[:])
                return
            for i in range(start, n+1):
                # 组合的话, 为了防止重复, 已遍历的数字不要重新遍历
                path.append(i)
                backtrack(path[-1]+1, k-1, res, path)
                path.pop()

        if (n < k) or n == 0 or k == 0:
            return []
        res = []
        backtrack(1, k, res, [])
        return res

if __name__ == "__main__":
    s = Solution().combine(4,2)
    print(s)

# @lc code=end

