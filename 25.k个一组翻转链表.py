# -*- coding:utf-8 -*-#
# @lc app=leetcode.cn id=25 lang=python3
#
# [25] k个一组翻转链表
#
# https://leetcode-cn.com/problems/reverse-nodes-in-k-group/description/
#
# algorithms
# Hard (49.82%)
# Total Accepted:    7.9K
# Total Submissions: 15.8K
# Testcase Example:  '[1,2,3,4,5]\n2'
#
# 给出一个链表，每 k 个节点一组进行翻转，并返回翻转后的链表。
#
# k 是一个正整数，它的值小于或等于链表的长度。如果节点总数不是 k 的整数倍，那么将最后剩余节点保持原有顺序。
#
# 示例 :
#
# 给定这个链表：1->2->3->4->5
#
# 当 k = 2 时，应当返回: 2->1->4->3->5
#
# 当 k = 3 时，应当返回: 3->2->1->4->5
#
# 说明 :
#
#
# 你的算法只能使用常数的额外空间。
# 你不能只是单纯的改变节点内部的值，而是需要实际的进行节点交换。
#
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


class Solution:
    def reverseKGroup(self, head, k):
        """
        :type head: ListNode
        :type k: int
        :rtype: ListNode

        思路：每次反转k个链表，如果不满k个则说明到达末尾，对这一次重新反转使之保持原有顺序
        """
        if not head or k <= 1:
            return head

        new_head = ListNode(None)
        new_head.next = head
        sub_head = new_head.next   # 当前段头部
        p = new_head   # 当前段前一个位置
        while sub_head:
            try:
                # 反转当前段: 将段头部之后的节点逐个插入到段前的位置
                for _ in range(k-1):
                    tmp = sub_head.next  # 保持要移动的节点
                    sub_head.next = sub_head.next.next  # 删除改节点
                    tmp.next = p.next  # 接上节点尾部
                    p.next = tmp  # 接上节点头部
            except AttributeError:
                # 最后不满k个, 此时最后一段已经反转
                sub_head = p.next  # 将段头指向反转后的头部
                while sub_head.next:
                    tmp = sub_head.next
                    sub_head.next = sub_head.next.next
                    tmp.next = p.next
                    p.next = tmp
                break
            p = sub_head
            sub_head = sub_head.next
        return new_head.next

if __name__ == "__main__":
    l = build_list_node(range(11))
    print(Solution().reverseKGroup(l, 3))

