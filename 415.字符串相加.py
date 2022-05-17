#
# @lc app=leetcode.cn id=415 lang=python3
#
# [415] 字符串相加
#
# https://leetcode-cn.com/problems/add-strings/description/
#
# algorithms
# Easy (54.46%)
# Likes:    563
# Dislikes: 0
# Total Accepted:    203.5K
# Total Submissions: 371.6K
# Testcase Example:  '"11"\n"123"'
#
# 给定两个字符串形式的非负整数 num1 和num2 ，计算它们的和并同样以字符串形式返回。
#
# 你不能使用任何內建的用于处理大整数的库（比如 BigInteger）， 也不能直接将输入的字符串转换为整数形式。
#
#
#
# 示例 1：
#
#
# 输入：num1 = "11", num2 = "123"
# 输出："134"
#
#
# 示例 2：
#
#
# 输入：num1 = "456", num2 = "77"
# 输出："533"
#
#
# 示例 3：
#
#
# 输入：num1 = "0", num2 = "0"
# 输出："0"
#
#
#
#
#
#
# 提示：
#
#
# 1 <= num1.length, num2.length <= 10^4
# num1 和num2 都只包含数字 0-9
# num1 和num2 都不包含任何前导零
#
#
#

# @lc code=start
class Solution:
    def addStrings(self, num1: str, num2: str) -> str:
        """
        按每个字符计算, 并注意进位
        """

        ret = []
        length = max(len(num1), len(num2))
        tmp = 0
        for i in range(1, length+1):
            if i > len(num1):
                a = 0
            else:
                a = int(num1[-i])
            if i > len(num2):
                b = 0
            else:
                b = int(num2[-i])
            tmp, a = divmod(a+b+tmp, 10)
            ret.append(str(a))
        if tmp:
            ret.append(str(tmp))
        return ''.join(ret[::-1])

# @lc code=end

