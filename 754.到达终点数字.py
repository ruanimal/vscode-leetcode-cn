#
# @lc app=leetcode.cn id=754 lang=python3
#
# [754] 到达终点数字
#
# https://leetcode-cn.com/problems/reach-a-number/description/
#
# algorithms
# Medium (43.71%)
# Likes:    176
# Dislikes: 0
# Total Accepted:    10.2K
# Total Submissions: 23K
# Testcase Example:  '2'
#
# 在一根无限长的数轴上，你站在0的位置。终点在target的位置。
#
# 你可以做一些数量的移动 numMoves :
#
#
# 每次你可以选择向左或向右移动。
# 第 i 次移动（从  i == 1 开始，到 i == numMoves ），在选择的方向上走 i 步。
#
#
# 给定整数 target ，返回 到达目标所需的 最小 移动次数(即最小 numMoves ) 。
#
#
#
# 示例 1:
#
#
# 输入: target = 2
# 输出: 3
# 解释:
# 第一次移动，从 0 到 1 。
# 第二次移动，从 1 到 -1 。
# 第三次移动，从 -1 到 2 。
#
#
# 示例 2:
#
#
# 输入: target = 3
# 输出: 2
# 解释:
# 第一次移动，从 0 到 1 。
# 第二次移动，从 1 到 3 。
#
#
#
#
# 提示:
#
#
# -10^9 <= target <= 10^9
# target != 0
#
#
#

# @lc code=start

'''给你一个数，第n次可以向左走，也可以向右走，问你最少多少次可以走到目的地

一开始我考虑的是广度优先遍历解决，但是这样的话由于target太大，内存超了，于是只好考虑其他的方法，思考过后我发现这题用数学的方法解决其实很简单，首先，要到达目的地一定会有向左和向右，我们假设一定有一个最好的方案，
a1,a2,a3…an,假如a1到an都是正数，那么它一定是最好的方案，
假如存在负数，那么可以看成把a1,a2…an里面的若干个数变成负数，然后到达target，

可以证明，当a1+a2..an-target为偶数的时候，只需要把a1,a2,…an里面的一个数变成负数就能到达目的地，这就是最好的方案

当a1+a2..an-target为奇数的时候，有两种情况，
    当n为偶数的时候，n+1为奇数，可以证明，当把a1,a2..an里面一个数变成负数之后，只要在加一个数就能到达target，也就是a1+a2…an+an+1一定可以到达target,
    当n为奇数的时候，可以证明当把a1,a2..an里面一个数变成负数之后只要在加两个个数就能到达target，也就是a1+a2…an+an+1+an+2,所以有以下算法
'''

# TODO(rlj): 分成往左和往右两个数组, 转化为0-1背包问题

class Solution(object):
    def reachNumber(self, target):
        """抄的答案"""

        target = abs(target)
        k = 0
        while target > 0:
            k += 1
            target -= k
        return k if (target % 2 == 0) else (k + 1 + k%2)

# @lc code=end

