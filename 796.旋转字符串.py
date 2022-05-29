#
# @lc app=leetcode.cn id=796 lang=python3
#
# [796] 旋转字符串
#
# https://leetcode-cn.com/problems/rotate-string/description/
#
# algorithms
# Easy (54.75%)
# Likes:    254
# Dislikes: 0
# Total Accepted:    68.5K
# Total Submissions: 108.5K
# Testcase Example:  '"abcde"\n"cdeab"'
#
# 给定两个字符串, s 和 goal。如果在若干次旋转操作之后，s 能变成 goal ，那么返回 true 。
#
# s 的 旋转操作 就是将 s 最左边的字符移动到最右边。 
#
#
# 例如, 若 s = 'abcde'，在旋转一次之后结果就是'bcdea' 。
#
#
#
#
# 示例 1:
#
#
# 输入: s = "abcde", goal = "cdeab"
# 输出: true
#
#
# 示例 2:
#
#
# 输入: s = "abcde", goal = "abced"
# 输出: false
#
#
#
#
# 提示:
#
#
# 1 <= s.length, goal.length <= 100
# s 和 goal 由小写英文字母组成
#
#
#

# @lc code=start
class SolutionA:
    def rotateString(self, s: str, goal: str) -> bool:
        """暴力集合法"""

        if not s and not goal:
            return True
        if len(s) != len(goal):
            return False

        cache = set()
        for i in range(len(s)):
            cache.add(s[i+1:] + s[:i+1])
        return goal in cache

class Solution:
    def rotateString(self, s: str, goal: str) -> bool:
        """如果goal是由s位移而来, 那么(s+s)一点会包含goal
        去掉s+s最后一位是防止goal的长度大于s
        """

        if len(s) != len(goal):
            return False
        return goal in (s+s)[:-1]
# @lc code=end

