#
# @lc app=leetcode.cn id=32 lang=python
#
# [32] 最长有效括号
#
# https://leetcode-cn.com/problems/longest-valid-parentheses/description/
#
# algorithms
# Hard (28.15%)
# Likes:    331
# Dislikes: 0
# Total Accepted:    21.2K
# Total Submissions: 74.9K
# Testcase Example:  '"(()"'
#
# 给定一个只包含 '(' 和 ')' 的字符串，找出最长的包含有效括号的子串的长度。
# 
# 示例 1:
# 
# 输入: "(()"
# 输出: 2
# 解释: 最长有效括号子串为 "()"
# 
# 
# 示例 2:
# 
# 输入: ")()())"
# 输出: 4
# 解释: 最长有效括号子串为 "()()"
# 
# 
#
class Solution(object):
    def longestValidParentheses(self, s):
        """
        :type s: str
        :rtype: int
        """
        tmp = 0
        stack = []
        for i in s:
            # print(stack, i, tmp)
            if i == '(':
                stack.append('(')
                continue
            while stack:
                x = stack.pop()
                if x == '(':
                    stack.append(tmp+2)
                    tmp = 0
                    break
                else:
                    tmp += x 
            if tmp != 0:
                stack.append(tmp)

            # elif stack:
            #     stack.pop()
            #     tmp += 2
            #     ans = max(tmp, ans)
            # else:
            #     tmp = 0
        print(stack)
        ans = 0
        tmp = 0
        for i in stack:
            print(tmp)
            if i == '(':
                tmp = 0 
                ans = max(tmp, ans) 
            else:
                tmp += i 
        return max(tmp, ans)
    
if __name__ == "__main__":
    s = Solution().longestValidParentheses(")()())()()(")
    print(s)

