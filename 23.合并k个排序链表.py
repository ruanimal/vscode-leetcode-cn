#
# @lc app=leetcode.cn id=23 lang=python3
#
# [23] 合并K个排序链表
#
# https://leetcode-cn.com/problems/merge-k-sorted-lists/description/
#
# algorithms
# Hard (43.30%)
# Total Accepted:    16.7K
# Total Submissions: 37.8K
# Testcase Example:  '[[1,4,5],[1,3,4],[2,6]]'
#
# 合并 k 个排序链表，返回合并后的排序链表。请分析和描述算法的复杂度。
#
# 示例:
#
# 输入:
# [
# 1->4->5,
# 1->3->4,
# 2->6
# ]
# 输出: 1->1->2->3->4->4->5->6
#
#
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None
try:
    from comm import *
except Exception:
    pass

from dataclasses import dataclass, field
from typing import Any

@dataclass(order=True)
class PrioritizedItem:
    priority: int
    item: Any=field(compare=False)

class Solution_MinHeap:
    def mergeKLists(self, lists: List[ListNode]) -> ListNode:
        """
        采用优先队列(最小堆), 比归并排序慢
        """
        import queue
        min_heap = queue.PriorityQueue()
        p = dummy = ListNode(-1)
        for node in lists:
            if node:
                min_heap.put(PrioritizedItem(node.val, node))
        while not min_heap.empty():
            wrap = min_heap.get()
            node = wrap.item
            p.next = node
            p = p.next
            node = node.next
            if node:
                min_heap.put(PrioritizedItem(node.val, node))
        return dummy.next

class Solution:
    def mergeKLists(self, lists: List[ListNode]) -> ListNode:
        """
        采用分治法
        """

        if len(lists) == 0:
            return None
        if len(lists) == 1:
            return lists[0]
        l1 = self.mergeKLists(lists[:len(lists)//2])
        l2 = self.mergeKLists(lists[len(lists)//2:])
        return self.mergeTwoLists(l1, l2)

    def mergeTwoLists(self, l1: ListNode, l2: ListNode) -> ListNode:
        """
        参考 21.合并两个有序链表.py
        """

        p1 = l1
        p2 = l2
        p = dummy = ListNode(None)

        while p1 and p2:
            if p1.val < p2.val:
                p.next = p1
                p1 = p1.next
            else:
                p.next = p2
                p2 = p2.next
            p = p.next
        p.next = p1 or p2
        return dummy.next


if __name__ == "__main__":
    pass

