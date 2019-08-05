class Solution:
    def tribonacci(self, n: int) -> int:
        dp = [0, 1, 1]
        if n < 0:
            return
        if n < 3:
            return dp[n]
        for i in range(3, n+1):
            tmp = dp[i - 3] + dp[i - 2] + dp[i - 1]
            dp.append(tmp)
        return dp[n]


if __name__ == "__main__":
    s = Solution().tribonacci(25)
    print(s)
    s = Solution().tribonacci(3)
    print(s)
