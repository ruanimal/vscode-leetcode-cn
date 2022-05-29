#
# @lc app=leetcode.cn id=874 lang=python3
#
# [874] 模拟行走机器人
#
# https://leetcode-cn.com/problems/walking-robot-simulation/description/
#
# algorithms
# Medium (42.17%)
# Likes:    164
# Dislikes: 0
# Total Accepted:    23.5K
# Total Submissions: 55.5K
# Testcase Example:  '[4,-1,3]\n[]'
#
# 机器人在一个无限大小的 XY 网格平面上行走，从点 (0, 0) 处开始出发，面向北方。该机器人可以接收以下三种类型的命令 commands
# ：
#
#
# -2 ：向左转 90 度
# -1 ：向右转 90 度
# 1  ：向前移动 x 个单位长度
#
#
# 在网格上有一些格子被视为障碍物 obstacles 。第 i 个障碍物位于网格点  obstacles[i] = (xi, yi) 。
#
# 机器人无法走到障碍物上，它将会停留在障碍物的前一个网格方块上，但仍然可以继续尝试进行该路线的其余部分。
#
# 返回从原点到机器人所有经过的路径点（坐标为整数）的最大欧式距离的平方。（即，如果距离为 5 ，则返回 25 ）
#
#
#
#
#
#
#
#
#
# 注意：
#
#
# 北表示 +Y 方向。
# 东表示 +X 方向。
# 南表示 -Y 方向。
# 西表示 -X 方向。
#
#
#
#
#
#
#
#
# 示例 1：
#
#
# 输入：commands = [4,-1,3], obstacles = []
# 输出：25
# 解释：
# 机器人开始位于 (0, 0)：
# 1. 向北移动 4 个单位，到达 (0, 4)
# 2. 右转
# 3. 向东移动 3 个单位，到达 (3, 4)
# 距离原点最远的是 (3, 4) ，距离为 3^2 + 4^2 = 25
#
# 示例 2：
#
#
# 输入：commands = [4,-1,4,-2,4], obstacles = [[2,4]]
# 输出：65
# 解释：机器人开始位于 (0, 0)：
# 1. 向北移动 4 个单位，到达 (0, 4)
# 2. 右转
# 3. 向东移动 1 个单位，然后被位于 (2, 4) 的障碍物阻挡，机器人停在 (1, 4)
# 4. 左转
# 5. 向北走 4 个单位，到达 (1, 8)
# 距离原点最远的是 (1, 8) ，距离为 1^2 + 8^2 = 65
#
#
#
# 提示：
#
#
# 1
# commands[i] is one of the values in the list [-2,-1,1,2,3,4,5,6,7,8,9].
# 0
# -3 * 10^4 i, yi
# 答案保证小于 2^31
#
#
#

from comm import *
# @lc code=start
class Solution:
    def robotSim(self, commands: List[int], obstacles: List[List[int]]) -> int:
        def check_turn(head, c):
            heads = [
                (0, 1),   # 朝向x, 正方向
                (1, 1),   # 朝向y, 正方向
                (0, -1),
                (1, -1),
            ]
            if c == -2:  # 左转
                next_head = (heads.index(head)+1) % 4
                return heads[next_head]
            elif c == -1:
                next_head = (heads.index(head)-1) % 4
                return heads[next_head]
            else:
                return

        marks = [set(), set()]
        obstacles_set = set()
        for x, y in obstacles:
            marks[0].add(y)
            marks[1].add(x)
            obstacles_set.add((x, y))

        head = (1, 1)  # 朝向
        pos = [0, 0]   # 当前位置
        ans = 0
        for i in commands:
            next_head = check_turn(head, i)
            if next_head:
                head = next_head
                continue

            if pos[head[0] ^ 1] not in marks[head[0]]:   # 没有挡路的
                pos[head[0]] += head[1] * i
                ans = max(ans, pos[0] ** 2 + pos[1] ** 2)
                continue

            for _ in range(i):
                pos[head[0]] += head[1] * 1
                if tuple(pos) in obstacles_set:
                    pos[head[0]] -= head[1] * 1
                    break
                ans = max(ans, pos[0] ** 2 + pos[1] ** 2)
        return ans
# @lc code=end

