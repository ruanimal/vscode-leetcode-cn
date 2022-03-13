# -*- coding:utf-8 -*-
#
# @lc app=leetcode.cn id=92 lang=python3
#
# [92] 反转链表 II
#
# https://leetcode-cn.com/problems/reverse-linked-list-ii/description/
#
# algorithms
# Medium (41.13%)
# Total Accepted:    7.6K
# Total Submissions: 18K
# Testcase Example:  '[1,2,3,4,5]\n2\n4'
#
# 反转从位置 m 到 n 的链表。请使用一趟扫描完成反转。
#
# 说明:
# 1 ≤ m ≤ n ≤ 链表长度。
#
# 示例:
#
# 输入: 1->2->3->4->5->NULL, m = 2, n = 4
# 输出: 1->4->3->2->5->NULL
#
#
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None


try:
    from comm import *
except ImportError:
    LOCAL_TEST = False


class Solution_A:
    def reverseBetween(self, head: ListNode, m: int, n: int) -> ListNode:
        """
        使用头指针, 先走m-1步
        将m+1到n的节点插入到m前面
        """

        if not head or not head.next:
            return head

        dummy = ptr = ListNode(None)
        dummy.next = head

        for _ in range(m-1):
            ptr = ptr.next
        edge_ptr = ptr.next
        for _ in range(n-m):
            tmp = edge_ptr.next
            edge_ptr.next = edge_ptr.next.next
            tmp.next = ptr.next
            ptr.next = tmp
        return dummy.next

class Solution:
    def reverseN(self, head: ListNode, n: int) -> ListNode:
        if n <= 1 or not head.next:
            self.successor = head.next
            return head
        others = head.next
        head.next = None
        new_head = self.reverseN(others, n-1)
        others.next = head
        head.next = self.successor
        return new_head

    def reverseBetween(self, head: ListNode, m: int, n: int) -> ListNode:
        if m == n:
            return head
        if m == 1:
            return self.reverseN(head, n)
        head.next = self.reverseBetween(head.next, m-1, n-1)
        return head


if LOCAL_TEST:
    l = build_list_node([3,5])
    # print(l)
    # print('---')
    # print(Solution().reverseN(l, 2))
    print(Solution().reverseBetween(l, 1, 2))
