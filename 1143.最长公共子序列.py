#
# @lc app=leetcode.cn id=1143 lang=python3
#
# [1143] 最长公共子序列
#
# https://leetcode-cn.com/problems/longest-common-subsequence/description/
#
# algorithms
# Medium (64.06%)
# Likes:    1043
# Dislikes: 0
# Total Accepted:    251.9K
# Total Submissions: 390.4K
# Testcase Example:  '"abcde"\n"ace"'
#
# 给定两个字符串 text1 和 text2，返回这两个字符串的最长 公共子序列 的长度。如果不存在 公共子序列 ，返回 0 。
#
# 一个字符串的 子序列
# 是指这样一个新的字符串：它是由原字符串在不改变字符的相对顺序的情况下删除某些字符（也可以不删除任何字符）后组成的新字符串。
#
#
# 例如，"ace" 是 "abcde" 的子序列，但 "aec" 不是 "abcde" 的子序列。
#
#
# 两个字符串的 公共子序列 是这两个字符串所共同拥有的子序列。
#
#
#
# 示例 1：
#
#
# 输入：text1 = "abcde", text2 = "ace"
# 输出：3
# 解释：最长公共子序列是 "ace" ，它的长度为 3 。
#
#
# 示例 2：
#
#
# 输入：text1 = "abc", text2 = "abc"
# 输出：3
# 解释：最长公共子序列是 "abc" ，它的长度为 3 。
#
#
# 示例 3：
#
#
# 输入：text1 = "abc", text2 = "def"
# 输出：0
# 解释：两个字符串没有公共子序列，返回 0 。
#
#
#
#
# 提示：
#
#
# 1
# text1 和 text2 仅由小写英文字符组成。
#
#
#

# @lc code=start
from collections import deque
class SolutionA:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        """转化成最长递增只序列
        从text2中找出text1中的每个字符出现的索引, 求索引数组的递增子序列
        不能存在多个字符串时, 有多种选择的问题
        """

        if len(text1) > len(text2):
            text1, text2 = text2, text1

        index_map = {}
        for idx, e in enumerate(text2):
            index_map.setdefault(e, deque()).append(idx)

        found = []
        for i in text1:
            if len(index_map.get(i, [])) > 0:
                print(i)
                found.append(index_map[i].popleft())
        print(found)
        if len(found) == 0:  # 防止没有重复元素的情况
            return 0

        dp = [1 for _ in found]
        for i in range(1, len(found)):
            for j in range(i):
                if found[i] > found[j]:
                    dp[i] = max(dp[i], dp[j]+1)
        return max(dp)

import functools

class SolutionB:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        '''递归法'''
        @functools.lru_cache
        def lcs(text1: str, text2: str, m: int, n: int):
            if m == 0 or n == 0:
                return 0
            if text1[m-1] == text2[n-1]:
                return lcs(text1, text2, m-1, n-1) + 1
            else:
                return max(lcs(text1, text2, m-1, n), lcs(text1, text2, m, n-1))
        return lcs(text1, text2, len(text1), len(text2))


class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        """转化成求编辑距离
        """

        m, n = len(text1), len(text2)
        f = [[0 for _ in range(n+1)] for _ in range(m+1)]
        for i in range(1, m+1):
            for j in range(1, n+1):
                if text1[i-1] == text2[j-1]:
                    f[i][j] = f[i-1][j-1] + 1
                else:
                    # max(text1删除i, text2删除j, i和j同时删除)
                    f[i][j] = max(f[i-1][j], f[i][j-1], f[i-1][j-1])
        return f[m][n]

# @lc code=end

s = Solution().longestCommonSubsequence("mhunuzqrkzsnidwbun", "szulspmhwpazoxijwbq")
print(s)
s = SolutionB().longestCommonSubsequence("mhunuzqrkzsnidwbun", "szulspmhwpazoxijwbq")
print(s)
