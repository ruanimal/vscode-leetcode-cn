#
# @lc app=leetcode.cn id=1025 lang=python
#
# [1025] 除数博弈
#
class Solution(object):
    def divisorGame(self, N):
        """
        :type N: int
        :rtype: bool
        动态规划

        f[N]: 数字N时能否获胜, 当博弈次数为奇数时爱丽丝获胜
        f[N] = True if any(f[N-x]==False) for x in (N的约数) else False
        """
        f = {}
        f[1] = 0
        f[2] = 1
        f[3] = 0
        for i in range(4, N+1):
            f[i] = 0
            for j in range(1, i):
                if i % j != 0:
                    continue
                print(i, j)
                if f[i-j] == 0:
                    f[i] = 1
                    break
        return bool(f[N])


if __name__ == "__main__":
    s = Solution().divisorGame(100)
    print(s)
