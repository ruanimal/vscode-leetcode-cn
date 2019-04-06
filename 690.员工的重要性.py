#
# @lc app=leetcode.cn id=690 lang=python
#
# [690] 员工的重要性
#
# https://leetcode-cn.com/problems/employee-importance/description/
#
# algorithms
# Easy (47.50%)
# Total Accepted:    2.8K
# Total Submissions: 5.7K
# Testcase Example:  '[[1,2,[2]], [2,3,[]]]\n2'
#
# 给定一个保存员工信息的数据结构，它包含了员工唯一的id，重要度 和 直系下属的id。
#
# 比如，员工1是员工2的领导，员工2是员工3的领导。他们相应的重要度为15, 10, 5。那么员工1的数据结构是[1, 15,
# [2]]，员工2的数据结构是[2, 10, [3]]，员工3的数据结构是[3, 5,
# []]。注意虽然员工3也是员工1的一个下属，但是由于并不是直系下属，因此没有体现在员工1的数据结构中。
#
# 现在输入一个公司的所有员工信息，以及单个员工id，返回这个员工和他所有下属的重要度之和。
#
# 示例 1:
#
#
# 输入: [[1, 5, [2, 3]], [2, 3, []], [3, 3, []]], 1
# 输出: 11
# 解释:
# 员工1自身的重要度是5，他有两个直系下属2和3，而且2和3的重要度均为3。因此员工1的总重要度是 5 + 3 + 3 = 11。
#
#
# 注意:
#
#
# 一个员工最多有一个直系领导，但是可以有多个直系下属
# 员工数量不超过2000。
#
#
#
"""
# Employee info
"""
class Employee(object):
    def __init__(self, id, importance, subordinates):
        # It's the unique id of each node.
        # unique id of this employee
        self.id = id
        # the importance value of this employee
        self.importance = importance
        # the id of direct subordinates
        self.subordinates = subordinates

    def __repr__(self):
        return 'Employee(%r, %r, %r)' % (self.id, self.importance, self.subordinates)

class Solution(object):
    def getImportance(self, employees, id):
        """
        :type employees: Employee
        :type id: int
        :rtype: int
        """
        def count_total(node):
            if not node.subordinates:
                node.total_importance = node.importance
                return node.total_importance

            node.total_importance = node.importance + sum([count_total(e_map[i]) for i in node.subordinates])
            return node.total_importance

        e_map = {i.id:i for i in employees}
        e = e_map[id]
        return count_total(e)

if __name__ == "__main__":
    data = [Employee(101, 3, []), Employee(2, 5, [101])]
    s = Solution().getImportance(data, 2)
    print(s)
    data = [Employee(1, 5, [2,3]), Employee(2, 3, []), Employee(3, 3, [])]
    s = Solution().getImportance(data, 1)
    print(s)
