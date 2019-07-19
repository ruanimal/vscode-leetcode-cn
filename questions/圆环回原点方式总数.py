#!/usr/bin/env python
# -*- coding:utf-8 -*-

def solution(k):
    """
    https://blog.csdn.net/hanyajun0123/article/details/84320469

    一个0到9十个点围成一圈， 从0开始，走k步，每一步可以顺时针也可以逆时针，问回到0点有几种走法

    使用动态规划

    状态dp[x][y] 到达, x, y 状态的走法数目
    终点状态 dp[k][0], 走k步正好到达0点
    最后一步 dp[k-1][1] 或者 dp[k-1][9], 得dp[x][y] = dp[x-1][y-1] + dp[x-1][y+1]
    存在循环, 所以 dp[x][y] = dp[x-1][(y-1) % 10] + dp[x-1][(y+1) % 10]
    """
    dp = [[0 for x in range(10)] for y in range(k+1)]
    dp[0][0] = 1
    for x in range(1, k+1):
        for y in range(10):
            dp[x][y] = dp[x-1][(y-1) % 10] + dp[x-1][(y+1) % 10]
    return dp[k][0]

if __name__ == "__main__":
    print(solution(4))
