#
# @lc app=leetcode.cn id=917 lang=python3
#
# [917] 仅仅反转字母
#
# https://leetcode-cn.com/problems/reverse-only-letters/description/
#
# algorithms
# Easy (60.27%)
# Likes:    170
# Dislikes: 0
# Total Accepted:    68.3K
# Total Submissions: 113.6K
# Testcase Example:  '"ab-cd"'
#
# 给你一个字符串 s ，根据下述规则反转字符串：
#
#
# 所有非英文字母保留在原有位置。
# 所有英文字母（小写或大写）位置反转。
#
#
# 返回反转后的 s 。
#
#
#
#
#
#
# 示例 1：
#
#
# 输入：s = "ab-cd"
# 输出："dc-ba"
#
#
#
#
#
# 示例 2：
#
#
# 输入：s = "a-bC-dEf-ghIj"
# 输出："j-Ih-gfE-dCba"
#
#
#
#
#
# 示例 3：
#
#
# 输入：s = "Test1ng-Leet=code-Q!"
# 输出："Qedo1ct-eeLg=ntse-T!"
#
#
#
#
# 提示
#
#
# 1 <= s.length <= 100
# s 仅由 ASCII 值在范围 [33, 122] 的字符组成
# s 不含 '\"' 或 '\\'
#
#
#

# @lc code=start
class Solution:
    def reverseOnlyLetters(self, s: str) -> str:
        """暴力实现
        可用双指针优化
        """

        stack = []
        index_que = []
        ret = []
        for idx, i in enumerate(s):
            if i.isalpha():
                stack.append(i)
                ret.append(None)
                index_que.append(idx)
            else:
                ret.append(i)
        for i in index_que:
            ret[i] = stack.pop()
        return ''.join(ret)

# @lc code=end

