#
# @lc app=leetcode.cn id=148 lang=python3
#
# [148] 排序链表
#
# https://leetcode-cn.com/problems/sort-list/description/
#
# algorithms
# Medium (57.63%)
# Total Accepted:    8.9K
# Total Submissions: 15.2K
# Testcase Example:  '[4,2,1,3]'
#
# 在 O(n log n) 时间复杂度和常数级空间复杂度下，对链表进行排序。
#
# 示例 1:
#
# 输入: 4->2->1->3
# 输出: 1->2->3->4
#
#
# 示例 2:
#
# 输入: -1->5->3->4->0
# 输出: -1->0->3->4->5
#
#
# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None


from comm import *
# @lc code=start


class Solution(object):
    def sortList(self, head: ListNode) -> ListNode:
        """归并排序"""
        def merge(left, right):
            p1 = left
            p2 = right
            p = head = ListNode(None)
            while p1 and p2:
                if p1.val < p2.val:
                    p.next = p1
                    p1 = p1.next
                else:
                    p.next = p2
                    p2 = p2.next
                p = p.next
            p1 = p1 or p2 or None
            while p1:
                p.next = p1
                p = p.next
                p1 = p1.next
            return head.next

        if not head or not head.next:
            return head

        fast_ptr = slow_ptr = head
        while fast_ptr.next and fast_ptr.next.next:
            slow_ptr = slow_ptr.next
            fast_ptr = fast_ptr.next.next
        left, right = head, slow_ptr.next
        slow_ptr.next = None
        return merge(self.sortList(left), self.sortList(right))

# @lc code=end

if __name__ == "__main__":
    l = build_list_node(range(9, -1, -1))
    print(Solution().sortList(l))

