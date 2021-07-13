#
# @lc app=leetcode.cn id=1622 lang=python
#
# [1622] 奇妙序列
#
# https://leetcode-cn.com/problems/fancy-sequence/description/
#
# algorithms
# Hard (14.55%)
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

class Fancy(object):

    def __init__(self):
        self.array = []
        self.operations = []
        self.op_index = []

    def append(self, val):
        """
        :type val: int
        :rtype: None
        """
        self.array.append(val)
        self.op_index.append(len(self.operations))

    def addAll(self, inc):
        """
        :type inc: int
        :rtype: None
        """
        self.operations.append((1, inc))

    def multAll(self, m):
        """
        :type m: int
        :rtype: None
        """
        self.operations.append((m, 0))

    def calc(self, idx):
        base = self.array[idx]
        for i in range(self.op_index[idx], len(self.operations)):
            a, b = self.operations[i]
            base = base * a + b
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


class FancyBak(object):

    def __init__(self):
        self.array = []
        self.operations = []
        self.op_index = []
        self.coef_list = [(1, 0)]  # getIndex(x) = ax + b

    def append(self, val):
        """
        :type val: int
        :rtype: None
        """
        self.array.append(val)
        self.op_index.append(len(self.operations)-1)

    def addAll(self, inc):
        """
        :type inc: int
        :rtype: None
        """
        # (pre_a * x + pre_a * b) x
        #
        a, b = 1, inc
        pre_a, pre_b = self.coef_list[-1]
        self.coef_list.append((pre_a*a, pre_b * b + b))

    def multAll(self, m):
        """
        :type m: int
        :rtype: None
        """
        a, b = m, 0
        pre_a, pre_b = self.coef_list[-1]
        self.coef_list.append((pre_a*a, pre_b * b + b))

    def calc(self, idx):
        base = self.array[idx]
        a1, b1 = self.operations[self.op_index[idx]]
        a2, b2 = self.operations[-1]
        return a2 * base + b2 - (a1 * base - b1)

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
fancy = Fancy()
fancy.append(2);   # 奇妙序列：[2]
fancy.addAll(3);   # 奇妙序列：[2+3] -> [5]
fancy.append(7);   # 奇妙序列：[5, 7]
fancy.multAll(2);  # 奇妙序列：[5*2, 7*2] -> [10, 14]
# import ipdb; ipdb.set_trace()
print(fancy.getIndex(1)); # 返回 10
print(fancy.getIndex(0)); # 返回 10
fancy.addAll(3);   # 奇妙序列：[10+3, 14+3] -> [13, 17]
fancy.append(10);  # 奇妙序列：[13, 17, 10]
fancy.multAll(2);  # 奇妙序列：[13*2, 17*2, 10*2] -> [26, 34, 20]
print(fancy.getIndex(0)); # 返回 26
# import ipdb; ipdb.set_trace()
print(fancy.getIndex(1)); # 返回 34
print(fancy.getIndex(2)); # 返回 20

# Your Fancy object will be instantiated and called as such:
# obj = Fancy()
# obj.append(val)
# obj.addAll(inc)
# obj.multAll(m)
# param_4 = obj.getIndex(idx)
# @lc code=end

