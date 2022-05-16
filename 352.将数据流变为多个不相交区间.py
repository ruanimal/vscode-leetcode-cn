#
# @lc app=leetcode.cn id=352 lang=python3
#
# [352] 将数据流变为多个不相交区间
#
# https://leetcode-cn.com/problems/data-stream-as-disjoint-intervals/description/
#
# algorithms
# Hard (67.69%)
# Likes:    159
# Dislikes: 0
# Total Accepted:    22.5K
# Total Submissions: 33.2K
# Testcase Example:  '["SummaryRanges","addNum","getIntervals","addNum","getIntervals","addNum","getIntervals","addNum","getIntervals","addNum","getIntervals"]\n' +
#   '[[],[1],[],[3],[],[7],[],[2],[],[6],[]]'
#
#  给你一个由非负整数 a1, a2, ..., an 组成的数据流输入，请你将到目前为止看到的数字总结为不相交的区间列表。
#
# 实现 SummaryRanges 类：
#
#
#
#
# SummaryRanges() 使用一个空数据流初始化对象。
# void addNum(int val) 向数据流中加入整数 val 。
# int[][] getIntervals() 以不相交区间 [starti, endi] 的列表形式返回对数据流中整数的总结。
#
#
#
#
# 示例：
#
#
# 输入：
# ["SummaryRanges", "addNum", "getIntervals", "addNum", "getIntervals",
# "addNum", "getIntervals", "addNum", "getIntervals", "addNum", "getIntervals"]
# [[], [1], [], [3], [], [7], [], [2], [], [6], []]
# 输出：
# [null, null, [[1, 1]], null, [[1, 1], [3, 3]], null, [[1, 1], [3, 3], [7,
# 7]], null, [[1, 3], [7, 7]], null, [[1, 3], [6, 7]]]
#
# 解释：
# SummaryRanges summaryRanges = new SummaryRanges();
# summaryRanges.addNum(1);      // arr = [1]
# summaryRanges.getIntervals(); // 返回 [[1, 1]]
# summaryRanges.addNum(3);      // arr = [1, 3]
# summaryRanges.getIntervals(); // 返回 [[1, 1], [3, 3]]
# summaryRanges.addNum(7);      // arr = [1, 3, 7]
# summaryRanges.getIntervals(); // 返回 [[1, 1], [3, 3], [7, 7]]
# summaryRanges.addNum(2);      // arr = [1, 2, 3, 7]
# summaryRanges.getIntervals(); // 返回 [[1, 3], [7, 7]]
# summaryRanges.addNum(6);      // arr = [1, 2, 3, 6, 7]
# summaryRanges.getIntervals(); // 返回 [[1, 3], [6, 7]]
#
#
#
#
# 提示：
#
#
# 0 <= val <= 10^4
# 最多调用 addNum 和 getIntervals 方法 3 * 10^4 次
#
#
#
#
#
#
# 进阶：如果存在大量合并，并且与数据流的大小相比，不相交区间的数量很小，该怎么办?
#
#

from comm import *

# @lc code=start

class SummaryRanges:
    def __init__(self):
        self.data = [[-10, -10], [10010, 10010]]  # 最大边界和最小边界, 简化越界处理

    def addNum(self, val: int) -> None:
        left = 0
        right = len(self.data)-1
        while left < right:
            mid = (left+right) >> 1
            if self.data[mid][0] < val:
                left = mid + 1
            else:
                right = mid
        # self.data[left][0] >= val
        # 如: [(1, 1), (4, 4)] add 3
        # 我们找到一个区间 (self.data[left-1][0], self.data[left][0]]
        # val所在区间有下面5种情况
        # (start1, end1], [end1+1, end1+1] (end1+1, start2-1) [start2-1, start2-1] [start2, start2]
        if self.data[left][0] == val:  # 已存在
            return
        if self.data[left-1][1] >= val: # (start1, end1]
            return
        # (end1+1, start2-1) 且区间没有位置, 如[[1, 1], [3,3]], addNum(2)
        # 此时 end1+1 == start2-1, 也就是中间3种情况合并了, 所以得合并区间, 否则相邻的边界就重复了
        if self.data[left-1][1]+1 == val == self.data[left][0]-1:
            self.data[left-1][1] = self.data[left][1]
            del self.data[left]
        elif self.data[left-1][1]+1 == val:   # [end1+1, end1+1], 扩展前一个区间的右边界
            self.data[left-1][1] += 1
        elif val == self.data[left][0]-1:  # [start2-1, start2-1], 扩展当前区间的的左边界
            self.data[left][0] -= 1
        else:   # (end1+1, start2-1) 且区间有位置, 插入
            self.data.insert(left, [val, val])

    def getIntervals(self) -> List[List[int]]:
        return self.data[1: -1]


# Your SummaryRanges object will be instantiated and called as such:
# obj = SummaryRanges()
# obj.addNum(val)
# param_2 = obj.getIntervals()
# @lc code=end

s = SummaryRanges()
s.addNum(1)
s.addNum(3)
s.addNum(9)
s.addNum(2)
s.addNum(3)
print(s.getIntervals())

# test = [[],[49],[],[97],[],[53],[],[5],[],[33],[],[65],[],[62],[],[51],[],[100],[],[38],[],[61],[],[45],[],[74],[],[27],[],[64],[],[17],[],[36],[],[17],[],[96],[],[12],[],[79],[],[32],[],[68],[],[90],[],[77],[],[18],[],[39],[],[12],[],[93],[],[9],[],[87],[],[42],[],[60],[],[71],[],[12],[],[45],[],[55],[],[40],[],[78],[],[81],[],[26],[],[70],[],[61],[],[56],[],[66],[],[33],[],[7],[],[70],[],[1],[],[11],[],[92],[],[51],[],[90],[],[100],[],[85],[],[80],[],[0],[],[78],[],[63],[],[42],[],[31],[],[93],[],[41],[],[90],[],[8],[],[24],[],[72],[],[28],[],[30],[],[18],[],[69],[],[57],[],[11],[],[10],[],[40],[],[65],[],[62],[],[13],[],[38],[],[70],[],[37],[],[90],[],[15],[],[70],[],[42],[],[69],[],[26],[],[77],[],[70],[],[75],[],[36],[],[56],[],[11],[],[76],[],[49],[],[40],[],[73],[],[30],[],[37],[],[23],[]]
# for i in test:
#     if i:
#         s.addNum(i[0])
#         print(i[0], s.getIntervals())
