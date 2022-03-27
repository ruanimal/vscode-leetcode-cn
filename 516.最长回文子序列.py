#
# @lc app=leetcode.cn id=516 lang=python3
#
# [516] 最长回文子序列
#
# https://leetcode-cn.com/problems/longest-palindromic-subsequence/description/
#
# algorithms
# Medium (66.12%)
# Likes:    755
# Dislikes: 0
# Total Accepted:    110.6K
# Total Submissions: 167.2K
# Testcase Example:  '"bbbab"'
#
# 给你一个字符串 s ，找出其中最长的回文子序列，并返回该序列的长度。
#
# 子序列定义为：不改变剩余字符顺序的情况下，删除某些字符或者不删除任何字符形成的一个序列。
#
#
#
# 示例 1：
#
#
# 输入：s = "bbbab"
# 输出：4
# 解释：一个可能的最长回文子序列为 "bbbb" 。
#
#
# 示例 2：
#
#
# 输入：s = "cbbd"
# 输出：2
# 解释：一个可能的最长回文子序列为 "bb" 。
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

# @lc code=start
class Solution:
    def longestPalindromeSubseq(self, s: str) -> int:
        """
        dp[i][j] s[i:j+1] 的最长子序列长度
        则
            s[i] == s[j] => dp[i+1][j-1] + 2
            s[i] != s[j] => max(dp[i+1][j], dp[i][j-1])
        """

        length = len(s)
        if length <= 1:
            return length

        dp = [[0] * length for _ in range(length)]
        for x in range(length-1, -1, -1):
            dp[x][x] = 1
            for y in range(x+1, length):
                if s[x] == s[y]:
                    dp[x][y] = dp[x+1][y-1] + 2
                else:
                    dp[x][y] = max(dp[x+1][y], dp[x][y-1])

        # print(dp)
        return dp[0][length-1]

# @lc code=end

s = Solution()
print(s.longestPalindromeSubseq('data'))
