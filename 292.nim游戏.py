#
# @lc app=leetcode.cn id=292 lang=python3
#
# [292] Nim游戏
#
# https://leetcode-cn.com/problems/nim-game/description/
#
# algorithms
# Easy (65.93%)
# Total Accepted:    13K
# Total Submissions: 19.4K
# Testcase Example:  '4'
#
# 你和你的朋友，两个人一起玩 Nim游戏：桌子上有一堆石头，每次你们轮流拿掉 1 - 3 块石头。 拿掉最后一块石头的人就是获胜者。你作为先手。
#
# 你们是聪明人，每一步都是最优解。 编写一个函数，来判断你是否可以在给定石头数量的情况下赢得游戏。
#
# 示例:
#
# 输入: 4
# 输出: false
# 解释: 如果堆中有 4 块石头，那么你永远不会赢得比赛；
# 因为无论你拿走 1 块、2 块 还是 3 块石头，最后一块石头总是会被你的朋友拿走。
#
#
#
class Solution(object):
    def canWinNim(self, n: int) -> bool:
        """
        如果石头是4的倍数, 那么等你拿了a个之后, 他可以拿4-a个, 最终和4个的情况是一样的, 对手赢
        """
        return n % 4 != 0

