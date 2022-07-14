#
# @lc app=leetcode.cn id=583 lang=python3
#
# [583] 两个字符串的删除操作
#
# https://leetcode-cn.com/problems/delete-operation-for-two-strings/description/
#
# algorithms
# Medium (63.58%)
# Likes:    458
# Dislikes: 0
# Total Accepted:    86.6K
# Total Submissions: 132.6K
# Testcase Example:  '"sea"\n"eat"'
#
# 给定两个单词 word1 和 word2 ，返回使得 word1 和  word2 相同所需的最小步数。
#
# 每步 可以删除任意一个字符串中的一个字符。
#
#
#
# 示例 1：
#
#
# 输入: word1 = "sea", word2 = "eat"
# 输出: 2
# 解释: 第一步将 "sea" 变为 "ea" ，第二步将 "eat "变为 "ea"
#
#
# 示例  2:
#
#
# 输入：word1 = "leetcode", word2 = "etco"
# 输出：4
#
#
#
#
# 提示：
#
#
#
# 1 <= word1.length, word2.length <= 500
# word1 和 word2 只包含小写英文字母
#
#
#

# @lc code=start
class SolutionA:
    def minDistance(self, word1: str, word2: str) -> int:
        """递归, 超时, 便于理解dp(抄的)
        求最小步数, 其实就是求最长相同字符串
        """

        def lcs(s1, s2, m, n):
            if m == 0 or n == 0:
                return 0
            elif s1[m-1] == s2[n-1]:
                return 1 + lcs(s1, s2, m-1, n-1)  # 都保留
            else:
                return max(lcs(s1,s2, m-1,n), lcs(s1,s2,m,n-1))  # 保留word1的字符,还是word2的字符
        return len(word1) + len(word2) - 2 * lcs(word1, word2, len(word1), len(word2))

class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        m, n = len(word1), len(word2)
        f = [[999 for _ in range(n+1)] for _ in range(m+1)]
        pass
# @lc code=end

s = SolutionA().minDistance(word1 = "leetcode", word2 = "et1co")
print(s)
