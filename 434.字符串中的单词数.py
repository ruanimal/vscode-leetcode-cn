#
# @lc app=leetcode.cn id=434 lang=python3
#
# [434] 字符串中的单词数
#
# https://leetcode-cn.com/problems/number-of-segments-in-a-string/description/
#
# algorithms
# Easy (30.12%)
# Likes:    34
# Dislikes: 0
# Total Accepted:    6K
# Total Submissions: 19.5K
# Testcase Example:  '"Hello, my name is John"'
#
# 统计字符串中的单词个数，这里的单词指的是连续的不是空格的字符。
#
# 请注意，你可以假定字符串里不包括任何不可打印的字符。
#
# 示例:
#
# 输入: "Hello, my name is John"
# 输出: 5
#
#
#
class Solution(object):
    def countSegments(self, s: str) -> int:
        """注意对状态的思考
        """
        in_word = False
        ans = 0
        for i in s:
            if in_word:
                if i != ' ':
                    continue
                else:
                    in_word = False
            else:
                if i != ' ':
                    ans += 1
                    in_word = True
                else:
                    continue
        return ans

if __name__ == "__main__":
    s = Solution().countSegments("love live! mu\'sic forever")
    print(s)
    s = Solution().countSegments( "H")
    print(s)
    s = Solution().countSegments( "")
    print(s)

