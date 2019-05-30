#
# @lc app=leetcode.cn id=122 lang=python
#
# [122] 买卖股票的最佳时机 II
#
class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        求最大单调递增区间， 将区间的右值减去左值， 然后再相加
        """
        ans = 0
        buy = sale = None
        for i in range(len(prices)):
            if i == 0:
                a = 2**31
            else:
                a = prices[i-1]
            if i == len(prices)-1:
                c = 0
            else:
                c = prices[i+1]
            b = prices[i]
            if b == min(a, b, c):
                buy = b
            if b == max(a, b, c) and buy is not None:
                sale = b
            if buy is not None and sale is not None:
                ans += (sale-buy)
                buy = sale = None
        return ans

if __name__ == "__main__":
    s = Solution().maxProfit([7,1,5,3,6,4])
    print(s)
    s = Solution().maxProfit([1,2,3,4,5])
    print(s)
    s = Solution().maxProfit([1])
    print(s)


