#
# @lc app=leetcode.cn id=412 lang=python3
#
# [412] Fizz Buzz
#
# https://leetcode-cn.com/problems/fizz-buzz/description/
#
# algorithms
# Easy (71.23%)
# Likes:    177
# Dislikes: 0
# Total Accepted:    122.9K
# Total Submissions: 172.2K
# Testcase Example:  '3'
#
# 给你一个整数 n ，找出从 1 到 n 各个整数的 Fizz Buzz 表示，并用字符串数组 answer（下标从 1 开始）返回结果，其中：
#
#
# answer[i] == "FizzBuzz" 如果 i 同时是 3 和 5 的倍数。
# answer[i] == "Fizz" 如果 i 是 3 的倍数。
# answer[i] == "Buzz" 如果 i 是 5 的倍数。
# answer[i] == i （以字符串形式）如果上述条件全不满足。
#
#
#
#
# 示例 1：
#
#
# 输入：n = 3
# 输出：["1","2","Fizz"]
#
#
# 示例 2：
#
#
# 输入：n = 5
# 输出：["1","2","Fizz","4","Buzz"]
#
#
# 示例 3：
#
#
# 输入：n = 15
#
# 输出：["1","2","Fizz","4","Buzz","Fizz","7","8","Fizz","Buzz","11","Fizz","13","14","FizzBuzz"]
#
#
#
# 提示：
#
#
# 1 <= n <= 10^4
#
#
#

from comm import *
# @lc code=start
class SolutionA:
    def fizzBuzz(self, n: int) -> List[str]:
        """暴力法
        """

        ans = []
        for i in range(1, n+1):
            if i % 15 == 0:
                ans.append("FizzBuzz")
            elif i % 3 == 0:
                ans.append("Fizz")
            elif i % 5 == 0:
                ans.append("Buzz")
            else:
                ans.append(str(i))
        return ans

class Solution:
    def fizzBuzz(self, n: int) -> List[str]:
        """取余查表法"""

        bases = ["FizzBuzz", "", "", "Fizz", "", "Buzz", "Fizz", "", "", "Fizz", "Buzz", "", "Fizz", "", ""]   # [15, 1-14]
        ans = []
        for i in range(1, n+1):
            t = i % 15
            if bases[t]:
                ans.append(bases[t])
            else:
                ans.append(str(i))
        return ans
# @lc code=end

