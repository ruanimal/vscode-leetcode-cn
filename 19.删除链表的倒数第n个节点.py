# -*- coding:utf-8 -*-
# @lc app=leetcode.cn id=19 lang=python3
#
# [19] 删除链表的倒数第N个节点
#
# https://leetcode-cn.com/problems/remove-nth-node-from-end-of-list/description/
#
# algorithms
# Medium (32.60%)
# Total Accepted:    33.9K
# Total Submissions: 103.8K
# Testcase Example:  '[1,2,3,4,5]\n2'
#
# 给定一个链表，删除链表的倒数第 n 个节点，并且返回链表的头结点。
#
# 示例：
#
# 给定一个链表: 1->2->3->4->5, 和 n = 2.
#
# 当删除了倒数第二个节点后，链表变为 1->2->3->5.
#
#
# 说明：
#
# 给定的 n 保证是有效的。
#
# 进阶：
#
# 你能尝试使用一趟扫描实现吗？
#
#
# Definition for singly-linked list.

try:
    from comm import *
except ImportError:
    LOCAL_TEST = False


class Solution:
    def removeNthFromEnd(self, head: ListNode, n: int) -> ListNode:
        """
        快慢指针

        """
        dummy = ListNode(None)
        dummy.next = head
        p1 = p2 = dummy

        while p2.next:
            if n > 0:
                p2 = p2.next
                n -= 1
            else:
                p2 = p2.next
                p1 = p1.next
        p1.next = p1.next.next
        return dummy.next

if LOCAL_TEST:
    n = build_list_node(range(10))
    print(n)
    head = build_list_node([1, 2, 3, 4, 5])
    print(Solution().removeNthFromEnd(head, 2))

