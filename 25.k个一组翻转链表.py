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


class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

    def __str__(self):
        tmp = []
        node = self
        while node:
            tmp.append(str(node.val))
            node = node.next
        return ' -> '.join(tmp)

    __repr__ = __str__


def build_list_node(nums):
    head = node = ListNode(None)
    for i in nums:
        node.next = ListNode(i)
        node = node.next
    return head.next


class Solution:
    def reverseKGroup(self, head: ListNode, k: int) -> ListNode:
        """k个一组翻转链表"""
        def recurse(head, newhead):  # 递归，head为原链表的头结点，newhead为反转后链表的头结点
            if head is None:
                return
            if head.next is None:
                newhead = head
            else:
                newhead = recurse(head.next, newhead)
                head.next.next = head
                head.next = None
            # print(newhead)
            return newhead

        if head is None:
            return
        if head.next is None:
            return head

        count = 1
        p = head
        pre_head = head
        new_head = None
        while p:
            count += 1
            p = p.next
            print(count)
            if count >= k:
                tmp = p.next
                print('tmp', tmp.val)
                p.next = None
                print('pre_head', pre_head)
                sub_link = recurse(pre_head, None)
                print('sub_link', sub_link)
                if new_head is None:
                    new_head = sub_link
                print('p', p.val)
                pre_head.next = tmp
                print('pre_head2', pre_head)
                print('new_head', new_head)
                p = pre_head
                pre_head = pre_head.next
                print('bb', new_head)
                print('c', p.val)
                count = 0
        return new_head


if __name__ == "__main__":
    l = build_list_node(range(10))
    print(Solution().reverseKGroup(l, 3))

