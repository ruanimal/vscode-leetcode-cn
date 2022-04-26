#
# @lc app=leetcode.cn id=17 lang=python3
#
# [17] 电话号码的字母组合
#
# https://leetcode-cn.com/problems/letter-combinations-of-a-phone-number/description/
#
# algorithms
# Medium (49.92%)
# Likes:    434
# Dislikes: 0
# Total Accepted:    42.2K
# Total Submissions: 82.9K
# Testcase Example:  '"23"'
#
# 给定一个仅包含数字 2-9 的字符串，返回所有它能表示的字母组合。
#
# 给出数字到字母的映射如下（与电话按键相同）。注意 1 不对应任何字母。
#
#
#
# 示例:
#
# 输入："23"
# 输出：["ad", "ae", "af", "bd", "be", "bf", "cd", "ce", "cf"].
#
#
# 说明:
# 尽管上面的答案是按字典序排列的，但是你可以任意选择答案输出的顺序。
#
#
class Solution_A(object):
    def letterCombinations(self, digits):
        """
        :type digits: str
        :rtype: List[str]
        """
        if not digits:
            return []

        digits_map = {
            '2': 'abc',
            '3': 'def',
            '4': 'ghi',
            '5': 'jkl',
            '6': 'mno',
            '7': 'pqrs',
            '8': 'tuv',
            '9': 'wxyz',
        }
        from itertools import product
        return [''.join(j) for j in product(*[digits_map[i] for i in digits])]

class Solution_B(object):
    def letterCombinations(self, digits):
        digits_map = {
            '2': 'abc',
            '3': 'def',
            '4': 'ghi',
            '5': 'jkl',
            '6': 'mno',
            '7': 'pqrs',
            '8': 'tuv',
            '9': 'wxyz',
        }
        data = [digits_map[i] for i in digits]
        def helper(data):
            if len(data) == 0:
                return []
            if len(data) == 1:
                return list(data[0])
            return [i + j for i in data[0] for j in helper(data[1:])]
        return helper(data)

class Solution(object):
    def letterCombinations(self, digits):
        digits_map = {
            '2': 'abc',
            '3': 'def',
            '4': 'ghi',
            '5': 'jkl',
            '6': 'mno',
            '7': 'pqrs',
            '8': 'tuv',
            '9': 'wxyz',
        }
        def backtrack(idx):
            if idx == len(strings):
                ans.append(''.join(track))
                return
            for i in strings[idx]:
                track.append(i)
                backtrack(idx+1)
                track.pop()

        if len(digits) == 0:
            return []
        strings = [digits_map[i] for i in digits]
        ans = []
        track = []
        backtrack(0)
        return ans

if __name__ == "__main__":
    s = Solution().letterCombinations('23')
    print(s)
    s = Solution().letterCombinations('2')
    print(s)
    s = Solution().letterCombinations('234')
    print(s)


