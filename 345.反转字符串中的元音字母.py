#
# @lc app=leetcode.cn id=345 lang=python3
#
# [345] 反转字符串中的元音字母
#
# https://leetcode-cn.com/problems/reverse-vowels-of-a-string/description/
#
# algorithms
# Easy (46.01%)
# Total Accepted:    7.7K
# Total Submissions: 16.6K
# Testcase Example:  '"hello"'
#
# 编写一个函数，以字符串作为输入，反转该字符串中的元音字母。
#
# 示例 1:
#
# 输入: "hello"
# 输出: "holle"
#
#
# 示例 2:
#
# 输入: "leetcode"
# 输出: "leotcede"
#
# 说明:
# 元音字母不包含字母"y"。
#
#


class SolutionA(object):
    def reverseVowels(self, s: str) -> str:
        """
        先找到元音的位置然后逐个交互
        """
        if len(s) < 2:
            return s
        string_list = list(s)
        vowels_list = [i for i, e in enumerate(s) if e in 'aeiouAEIOU']
        i = 0
        while i < len(vowels_list)/2:
            string_list[vowels_list[i]], string_list[vowels_list[-i-1]] = string_list[vowels_list[-i-1]], string_list[vowels_list[i]]
            i += 1
        return ''.join(string_list)

class Solution(object):
    vowels = set('aeiouAEIOU')

    def reverseVowels(self, s: str) -> str:
        """
        双指针
        """

        if len(s) < 2:
            return s
        tmp = list(s)
        i = 0
        j = len(tmp) - 1
        while i < j:
            if tmp[i] in self.vowels and tmp[j] in self.vowels:
                tmp[i], tmp[j] = tmp[j], tmp[i]
                i += 1
                j -= 1
            elif tmp[i] not in self.vowels:
                i += 1
            elif tmp[j] not in self.vowels:
                j -= 1
            else:
                i += 1
                j -= 1
        return ''.join(tmp)

s = Solution().reverseVowels('leetcode')
print(s)
