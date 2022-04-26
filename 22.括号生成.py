#
# @lc app=leetcode.cn id=22 lang=python3
#
# [22] 括号生成
#
# https://leetcode-cn.com/problems/generate-parentheses/description/
#
# algorithms
# Medium (69.88%)
# Likes:    424
# Dislikes: 0
# Total Accepted:    28.3K
# Total Submissions: 39.9K
# Testcase Example:  '3'
#
# 给出 n 代表生成括号的对数，请你写出一个函数，使其能够生成所有可能的并且有效的括号组合。
#
# 例如，给出 n = 3，生成结果为：
#
# [
# ⁠ "((()))",
# ⁠ "(()())",
# ⁠ "(())()",
# ⁠ "()(())",
# ⁠ "()()()"
# ]
#
#
#

# @lc code=start

class Solution_A(object):
    def generateParenthesis(self, n):
        """
        :type n: int
        :rtype: List[str]
        深度优先搜索 + 剪枝
        """
        if n < 1:
            return []

        ans = []
        def dfs(level, left, right, path):
            if level >= 2 * n:
                ans.append(''.join(path))
                return

            if left < n:
                path.append('(')
                dfs(level+1, left+1, right, path)
                path.pop()

            if left - 1 >= right:  # 左括号比右括号多一个以上
                path.append(')')
                dfs(level+1, left, right+1, path)
                path.pop()

        dfs(0, 0, 0, [])
        return ans

class Solution_B(object):
    def generateParenthesis(self, n):
        def backtrack(left, right):
            if len(track) == n*2:
                ans.append(''.join(track))
                return

            if left < n:
                track.append(L)
                backtrack(left+1, right)
                track.pop()
            if left - 1 >= right:
                track.append(R)
                backtrack(left, right+1)
                track.pop()

        ans = []
        track = []
        L, R = '()'
        backtrack(0, 0)
        return ans

class Solution(object):
    def generateParenthesis(self, n):
        def backtrack():
            if len(track) == n*2:
                ans.append(''.join(track))
                return

            for idx, i in enumerate(choices):
                if idx == 0 and used[0] >= n:   # 左括号用完了
                    continue
                if idx == 1 and used[0]-1 < used[1]:  # 右括号已经比左括号多两个, 如 ())
                    continue
                track.append(i)
                used[idx] += 1
                backtrack()
                used[idx] -= 1
                track.pop()

        ans = []
        track = []
        choices = '()'
        used = [0, 0]
        backtrack()
        return ans

# @lc code=end


if __name__ == "__main__":
    s = Solution().generateParenthesis(3)
    print(s)
    # s = Solution().generateParenthesis(4)
    # print(s)


