#
# @lc app=leetcode.cn id=985 lang=python
#
# [985] 查询后的偶数和
#
class Solution(object):
    def sumEvenAfterQueries(self, A, queries):
        """
        :type A: List[int]
        :type queries: List[List[int]]
        :rtype: List[int]
        """
        ret = []
        total_even = sum(x for x in A if x % 2 == 0)   # 还是前所有偶数的和
        for i, (val, index) in zip(A, queries):
            if A[index] % 2 == 0:  # 这个数原先是偶数, 前去掉它
                total_even -= A[index]
            A[index] += val
            if A[index] % 2 == 0:  # 增加后还是偶数
                total_even += A[index]
            ret.append(total_even)
        return ret

if __name__ == "__main__":
    s = Solution().sumEvenAfterQueries(A = [1,2,3,4], queries = [[1,0],[-3,1],[-4,0],[2,3]])
    print(s)
