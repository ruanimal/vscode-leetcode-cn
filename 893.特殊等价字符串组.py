#
# @lc app=leetcode.cn id=893 lang=python
#
# [893] 特殊等价字符串组
#
class Solution(object):
    def numSpecialEquivGroups(self, A):
        """
        :type A: List[str]
        :rtype: int
        题意: 对于A中的S, 如果S经过一定次数的移动后，可以变换到T，则S和T等价。

        对列表中的每个字符串，取其奇数位字符和偶数位字符分别排序。如果两个字符串特殊等价，则他们奇数位字符和偶数位字符排序后应该是相同的。
        """
        ans = set()
        for i in A:
            i_even = sorted(i[::2])
            i_odd = sorted(i[1:][::2])
            new_i = ''.join(i_even+i_odd)
            if new_i not in ans:
                ans.add(new_i)
        return len(ans)

if __name__ == "__main__":
    s = Solution().numSpecialEquivGroups(["abcd","cdab","adcb","cbad"])
    print(s)
