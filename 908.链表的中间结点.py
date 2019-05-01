#
# @lc app=leetcode.cn id=908 lang=python
#
# [908] 链表的中间结点
#
class Solution(object):
    def smallestRangeI(self, A, K):
        """
        :type A: List[int]
        :type K: int
        :rtype: int
        """
        # max_i = 0
        # min_i = 2 ** 31 - 1
        # for i in A:
        #     if i > max_i:
        #         max_i = i
        #     if i < min_i:
        #         min_i = i
        # if (max_i-min_i) <= 2*K:
        #     return 0
        # else:
        #     return max_i - min_i - 2*K
        max_i = max(A)
        min_i = min(A)
        if (max_i-min_i) <= 2*K:
            return 0
        else:
            return max_i - min_i - 2*K

if __name__ == "__main__":
    s = Solution().smallestRangeI(A = [1,3,6], K = 3)
    print(s)
    s = Solution().smallestRangeI(A = [0,10], K = 2)
    print(s)
    s = Solution().smallestRangeI(A = [1], K = 0)
    print(s)
    s = Solution().smallestRangeI(A = [3,1,10], K = 4)
    print(s)

