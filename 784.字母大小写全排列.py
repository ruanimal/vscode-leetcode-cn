#
# @lc app=leetcode.cn id=784 lang=python3
#
# [784] 字母大小写全排列
#
# https://leetcode-cn.com/problems/letter-case-permutation/description/
#
# algorithms
# Medium (69.53%)
# Likes:    386
# Dislikes: 0
# Total Accepted:    65K
# Total Submissions: 92.8K
# Testcase Example:  '"a1b2"'
#
# 给定一个字符串 s ，通过将字符串 s 中的每个字母转变大小写，我们可以获得一个新的字符串。
#
# 返回 所有可能得到的字符串集合 。以 任意顺序 返回输出。
#
#
#
# 示例 1：
#
#
# 输入：s = "a1b2"
# 输出：["a1b2", "a1B2", "A1b2", "A1B2"]
#
#
# 示例 2:
#
#
# 输入: s = "3z4"
# 输出: ["3z4","3Z4"]
#
#
#
#
# 提示:
#
#
# 1 <= s.length <= 12
# s 由小写英文字母、大写英文字母和数字组成
#
#
#

from comm import *

# @lc code=start

class Solution:
    def letterCasePermutation(self, S: str) -> List[str]:
        """dfs
        """
        ret = []
        tmp = []
        def dfs(pos):
            # print(tmp)
            if pos == len(S):
                ret.append(''.join(tmp))
                return
            if S[pos].isdigit():
                tmp.append(S[pos])
                dfs(pos+1)
                tmp.pop()
            elif S[pos].islower():
                tmp.append(S[pos])
                dfs(pos+1)
                tmp.pop()
                tmp.append(S[pos].upper())
                dfs(pos+1)
                tmp.pop()
            else:
                tmp.append(S[pos])
                dfs(pos+1)
                tmp.pop()
                tmp.append(S[pos].lower())
                dfs(pos+1)
                tmp.pop()
        dfs(0)
        return ret

class SolutionA:
    def letterCasePermutation(self, S: str) -> List[str]:
        """bfs
        """
        from collections import deque

        if not S:
            return

        tmp = deque()
        depth = 1
        if S[0].isdigit():
            tmp.append(S[0])
        else:
            tmp.append(S[0].lower())
            tmp.append(S[0].upper())

        for i in S[1:]:
            while depth and len(tmp[0]) == depth:
                x = tmp.popleft()
                if i.isdigit():
                    tmp.append(x + i)
                else:
                    tmp.append(x + i.lower())
                    tmp.append(x + i.upper())
            depth += 1
        return list(tmp)

# @lc code=end

if __name__ == "__main__":
    s = Solution().letterCasePermutation('a1b2')
    print(s)
