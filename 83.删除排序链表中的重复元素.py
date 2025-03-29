# -*- coding:utf-8 -*-
#
# @lc app=leetcode.cn id=83 lang=python3
#
# [83] 删除排序链表中的重复元素
#
# https://leetcode-cn.com/problems/remove-duplicates-from-sorted-list/description/
#
# algorithms
# Easy (44.38%)
# Total Accepted:    19.7K
# Total Submissions: 44.3K
# Testcase Example:  '[1,1,2]'
#
# 给定一个排序链表，删除所有重复的元素，使得每个元素只出现一次。
#
# 示例 1:
#
# 输入: 1->1->2
# 输出: 1->2
#
#
# 示例 2:
#
# 输入: 1->1->2->3->3
# 输出: 1->2->3
#
#
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

from comm import *

# @lc code=start


class Solution:
    def aa(self):
        return self.a

    def _deleteDuplicates(self, head: ListNode) -> ListNode:
        if not head:
            return
        if not head.next:
            return head
        ptr = head
        while ptr.next:
            if ptr.val == ptr.next.val:
                ptr.next = ptr.next.next
                continue
            ptr = ptr.next
        return head

    def deleteDuplicates(self, head: ListNode) -> ListNode:
        if not head:
            return
        head.next = self.deleteDuplicates(head.next)
        if head.next and head.val == head.next.val:
            return head.next
        return head

# @lc code=end

if __name__ == "__main__":
    l = build_list_node([1,1,2,2,2,3,4,4,6,8])
    print(Solution().deleteDuplicates(l))
    s = Solution()
    s.a = 1
    d = s.aa
    print(repr(d), s.aa(), d())


