#
# @lc app=leetcode.cn id=131 lang=python3
#
# [131] 分割回文串
#
# https://leetcode-cn.com/problems/palindrome-partitioning/description/
#
# algorithms
# Medium (72.43%)
# Likes:    776
# Dislikes: 0
# Total Accepted:    118.5K
# Total Submissions: 163.5K
# Testcase Example:  '"aab"'
#
# 给你一个字符串 s，请你将 s 分割成一些子串，使每个子串都是 回文串 。返回 s 所有可能的分割方案。
#
# 回文串 是正着读和反着读都一样的字符串。
#
#
#
# 示例 1：
#
#
# 输入：s = "aab"
# 输出：[["a","a","b"],["aa","b"]]
#
#
# 示例 2：
#
#
# 输入：s = "a"
# 输出：[["a"]]
#
#
#
#
# 提示：
#
#
# 1
# s 仅由小写英文字母组成
#
#
#
"""
gap: 0 1 2 3
str:  a a b

使用隔板法
对于长度为N的字符串, 可选分割点有开区间(0, N), 也就是1到N-1, 每个点位有分割和不分割两种选项
使用回溯法, 如果当前分割点构成的区间不是回文串,则剪枝

可以给 vaild 判断函数加上缓存 (动态规划), 理论上更快

"""


class Solution(object):
    def partition(self, s: str) -> list:
        def vaild(a, b):
            b = b-1
            while a < b:
                if s[a] != s[b]:
                    return False
                a += 1
                b -= 1
            return True

        def backtrack(res, path, level):
            if level == length:
                path.append(length)
                if len(path) > 1 and vaild(path[-2], path[-1]):
                    res.append([s[path[i]:path[i+1]] for i in range(len(path)-1)])
                path.pop()
                return

            # 取这个分割点
            if vaild(path[-1], level):
                path.append(level)
                backtrack(res, path, level+1)
                path.pop()
            # 不取这个分割点
            backtrack(res, path, level+1)

        length = len(s)
        if length == 0:
            return []
        res = []
        backtrack(res, [0], 1)
        return res

if __name__ == "__main__":
    s = Solution().partition('aab')
    print(s)

# @lc code=end
