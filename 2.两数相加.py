# -*- coding:utf-8 -*-
# @lc app=leetcode.cn id=2 lang=python3
#
# [2] 两数相加
#
# https://leetcode-cn.com/problems/add-two-numbers/description/
#
# algorithms
# Medium (33.30%)
# Total Accepted:    98.8K
# Total Submissions: 296.6K
# Testcase Example:  '[2,4,3]\n[5,6,4]'
#
# 给出两个 非空 的链表用来表示两个非负的整数。其中，它们各自的位数是按照 逆序 的方式存储的，并且它们的每个节点只能存储 一位 数字。
#
# 如果，我们将这两个数相加起来，则会返回一个新的链表来表示它们的和。
#
# 您可以假设除了数字 0 之外，这两个数都不会以 0 开头。
#
# 示例：
#
# 输入：(2 -> 4 -> 3) + (5 -> 6 -> 4)
# 输出：7 -> 0 -> 8
# 原因：342 + 465 = 807
#
#
#
from comm import *

# @lc code=start

class SolutionA:
    def addTwoNumbers(self, l1, l2):
        """
        按位加法实现, 循环法
        """

        if not l1:
            return l2
        if not l2:
            return l1

        p1 = l1
        p2 = l2
        p3 = head = ListNode(None)
        tmp = 0

        while p1 or p2:
            if p1:
                tmp += p1.val
                p1 = p1.next
            if p2:
                tmp += p2.val
                p2 = p2.next
            tmp, val = divmod(tmp, 10)
            p3.next = ListNode(val)
            p3 = p3.next
        if tmp:
            p3.next = ListNode(tmp)
        return head.next

class Solution:
    """递归解法"""

    def addTwoNumbers(self, l1: ListNode, l2: ListNode, carry=0):
        if not l1 and not l2 and carry==0:
            return None

        v1 = l1.val if l1 else 0
        v2 = l2.val if l2 else 0
        carry, current = divmod(v1 + v2 + carry, 10)
        node = ListNode(current)
        node.next = self.addTwoNumbers(l1.next if l1 else None, l2.next if l2 else None, carry)
        return node

# @lc code=end

if __name__ == "__main__":
    l1 = build_list_node([3])
    l2 = build_list_node([5, 6, 6])
    print(Solution().addTwoNumbers(l1, l2))
    pass

