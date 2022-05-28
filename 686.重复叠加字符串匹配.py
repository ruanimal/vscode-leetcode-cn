#
# @lc app=leetcode.cn id=686 lang=python3
#
# [686] 重复叠加字符串匹配
#
# https://leetcode-cn.com/problems/repeated-string-match/description/
#
# algorithms
# Medium (40.13%)
# Likes:    269
# Dislikes: 0
# Total Accepted:    45.1K
# Total Submissions: 112.5K
# Testcase Example:  '"abcd"\n"cdabcdab"'
#
# 给定两个字符串 a 和 b，寻找重复叠加字符串 a 的最小次数，使得字符串 b 成为叠加后的字符串 a 的子串，如果不存在则返回 -1。
#
# 注意：字符串 "abc" 重复叠加 0 次是 ""，重复叠加 1 次是 "abc"，重复叠加 2 次是 "abcabc"。
#
#
#
# 示例 1：
#
# 输入：a = "abcd", b = "cdabcdab"
# 输出：3
# 解释：a 重复叠加三遍后为 "abcdabcdabcd", 此时 b 是其子串。
#
#
# 示例 2：
#
# 输入：a = "a", b = "aa"
# 输出：2
#
#
# 示例 3：
#
# 输入：a = "a", b = "a"
# 输出：1
#
#
# 示例 4：
#
# 输入：a = "abc", b = "wxyz"
# 输出：-1
#
#
#
#
# 提示：
#
#
# 1 <= a.length <= 10^4
# 1 <= b.length <= 10^4
# a 和 b 由小写英文字母组成
#
#
#

# @lc code=start
class SolutionA:
    def repeatedStringMatch(self, A: str, B: str) -> int:
        """抄的答案, 不太懂"""

        if not A or not B:
            return -1
        i = 1
        a = A
        maxLen = len(A + A + B)
        while len(a) < maxLen:
            if (B in a):
                return i
            else:
                i = i + 1
                a += A
        return -1

# TODO(rlj): Rabin-Karp.
# TODO(rlj): KMP.
class Solution:
    def repeatedStringMatch(self, A: str, B: str) -> int:
        """
        B = subfix(A) + A * n + prefix(A), 其中n>=0
        """
        if not A or not B:
            return -1
        if B in A:      # subfix(A), A, prefix(A) 三者有其中之一的情况
            return 1
        if B in (A+A):  # subfix(A), A, prefix(A) 三者有其中之二的情况
            return 2

        ans = 0
        head_index = B.find(A)
        if head_index < 0:
            return -1
        i = head_index
        while i < len(B):   # 求完整A的个数
            if B.find(A, i) == i:
                i += len(A)
                ans += 1
            else:
                break
        tail_index = head_index + ans * len(A)
        if head_index > 0:   # n > 0 且有subfix
            if A.endswith(B[:head_index]):
                ans += 1
            else:
                return -1
        if tail_index < len(B):   # n > 0 有subfix
            if A.startswith(B[tail_index:]):
                ans += 1
            else:
                return -1
        return ans

# @lc code=end

if __name__ == "__main__":
    s = Solution().repeatedStringMatch('abcd', 'cdabcdabcdab')
    print(s)
    s = Solution().repeatedStringMatch('abcd', 'abcdabcdab')
    print(s)
    s = Solution().repeatedStringMatch('abcd', 'cdabcdacdabcda')
    print(s)
    s = Solution().repeatedStringMatch('aaaaaaaaaaaaaaaaaaaaaab', 'ba')
    print(s)
