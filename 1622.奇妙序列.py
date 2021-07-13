#
# @lc app=leetcode.cn id=1622 lang=python
#
# [1622] 奇妙序列
#
# https://leetcode-cn.com/problems/fancy-sequence/description/
#
# algorithms
# Hard (14.54%)
# Likes:    33
# Dislikes: 0
# Total Accepted:    2.1K
# Total Submissions: 14.2K
# Testcase Example:  '["Fancy","append","addAll","append","multAll","getIndex","addAll","append","multAll","getIndex","getIndex","getIndex"]\n' +
#   '[[],[2],[3],[7],[2],[0],[3],[10],[2],[0],[1],[2]]'
#
# 请你实现三个 API append，addAll 和 multAll 来实现奇妙序列。
#
# 请实现 Fancy 类 ：
#
#
# Fancy() 初始化一个空序列对象。
# void append(val) 将整数 val 添加在序列末尾。
# void addAll(inc) 将所有序列中的现有数值都增加 inc 。
# void multAll(m) 将序列中的所有现有数值都乘以整数 m 。
# int getIndex(idx) 得到下标为 idx 处的数值（下标从 0 开始），并将结果对 10^9 + 7
# 取余。如果下标大于等于序列的长度，请返回 -1 。
#
#
#
#
# 示例：
#
#
# 输入：
# ["Fancy", "append", "addAll", "append", "multAll", "getIndex", "addAll",
# "append", "multAll", "getIndex", "getIndex", "getIndex"]
# [[], [2], [3], [7], [2], [0], [3], [10], [2], [0], [1], [2]]
# 输出：
# [null, null, null, null, null, 10, null, null, null, 26, 34, 20]
#
# 解释：
# Fancy fancy = new Fancy();
# fancy.append(2);   // 奇妙序列：[2]
# fancy.addAll(3);   // 奇妙序列：[2+3] -> [5]
# fancy.append(7);   // 奇妙序列：[5, 7]
# fancy.multAll(2);  // 奇妙序列：[5*2, 7*2] -> [10, 14]
# fancy.getIndex(0); // 返回 10
# fancy.addAll(3);   // 奇妙序列：[10+3, 14+3] -> [13, 17]
# fancy.append(10);  // 奇妙序列：[13, 17, 10]
# fancy.multAll(2);  // 奇妙序列：[13*2, 17*2, 10*2] -> [26, 34, 20]
# fancy.getIndex(0); // 返回 26
# fancy.getIndex(1); // 返回 34
# fancy.getIndex(2); // 返回 20
#
#
#
#
# 提示：
#
#
# 1
# 0
# 总共最多会有 10^5 次对 append，addAll，multAll 和 getIndex 的调用。
#
#
#

# @lc code=start
MASK = 10**9 + 7
ADD = 0
MUL = 1

class Fancy(object):

    def __init__(self):
        self.array = []
        self.operations = []

    def append(self, val):
        """
        :type val: int
        :rtype: None
        """
        for idx in range(len(self.array)):
            self.array[idx] = self.calc(idx)
        self.operations = []
        self.array.append(val)

    def addAll(self, inc):
        """
        :type inc: int
        :rtype: None
        """
        self.operations.append((ADD, inc))

    def multAll(self, m):
        """
        :type m: int
        :rtype: None
        """
        self.operations.append((MUL, m))

    def calc(self, idx):
        base = self.array[idx]
        for op, val in self.operations:
            if op == ADD:
                base += val
            else:
                base *= val
        return base

    def getIndex(self, idx):
        """
        :type idx: int
        :rtype: int
        """
        if idx >= len(self.array):
            return -1
        return self.calc(idx) % MASK

    def __repr__(self):
        return '{!r}, {!r}'.format(self.array, self.operations)

# Your Fancy object will be instantiated and called as such:
# obj = Fancy()
# obj.append(val)
# obj.addAll(inc)
# obj.multAll(m)
# param_4 = obj.getIndex(idx)
# @lc code=end

