#
# @lc app=leetcode.cn id=412 lang=python
#
# [412] Fizz Buzz
#
class Solution(object):
    def fizzBuzz(self, n):
        """
        :type n: int
        :rtype: List[str]
        """
        # 正常版本
        # ans = []
        # for i in range(1, n+1):
        #     if i % 15 == 0:
        #         ans.append("FizzBuzz")
        #     elif i % 3 == 0:
        #         ans.append("Fizz")
        #     elif i % 5 == 0:
        #         ans.append("Buzz")
        #     else:
        #         ans.append(str(i))
        # return ans

        bases = ["FizzBuzz", "", "", "Fizz", "", "Buzz", "Fizz", "", "", "Fizz", "Buzz", "", "Fizz", "", ""]   # [15, 1-14]
        ans = []
        for i in range(1, n+1):
            t = i % 15
            if bases[t]:
                ans.append(bases[t])
            else:
                ans.append(str(i))
        return ans

if __name__ == "__main__":
    s = Solution().fizzBuzz(15)
    print(s)

