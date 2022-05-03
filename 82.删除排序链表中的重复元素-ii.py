#
# @lc app=leetcode.cn id=82 lang=python3
#
# [82] 删除排序链表中的重复元素 II
#
# https://leetcode-cn.com/problems/remove-duplicates-from-sorted-list-ii/description/
#
# algorithms
# Medium (39.09%)
# Total Accepted:    7.6K
# Total Submissions: 19.2K
# Testcase Example:  '[1,2,3,3,4,4,5]'
#
# 给定一个排序链表，删除所有含有重复数字的节点，只保留原始链表中 没有重复出现 的数字。
#
# 示例 1:
#
# 输入: 1->2->3->3->4->4->5
# 输出: 1->2->5
#
#
# 示例 2:
#
# 输入: 1->1->1->2->3
# 输出: 2->3
#
#
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None


from comm import *

# @lc code=start

class SolutionA:
    def deleteDuplicates(self, head: ListNode) -> ListNode:
        if not head:
            return
        if not head.next:
            return head

        new_head = ptr = ListNode(None)
        ptr.next = head
        if ptr.next.val == ptr.next.next.val:
            current_num = ptr.next.val
        else:
            current_num = None
        while ptr.next and ptr.next.next:
            if ptr.next.val == current_num:
                ptr.next = ptr.next.next
            elif ptr.next.val == ptr.next.next.val:
                current_num = ptr.next.val
            else:
                ptr = ptr.next
        if ptr.next.val == current_num:
            ptr.next = ptr.next.next
        return new_head.next

class Solution:
    def deleteDuplicates(self, head: ListNode) -> ListNode:
        """简化逻辑, 便于理解

        """

        if not head or not head.next:
            return head
        new_head = p2 = ListNode(None)

        p = head
        count = 1  # 包含当前点时, 等于当前数字的点有多少个
        while p and p.next:
            if p.val == p.next.val:
                count += 1
            else:   # 数字发生了变化
                if count == 1:   # 保留
                    p2.next = p
                    p2 = p2.next
                count = 1  # 重置计数
            p = p.next
        if count == 1:
            p2.next = p
        else:
            p2.next = None
        return new_head.next

# @lc code=end


if __name__ == "__main__":
    l = build_list_node([1, 1, 2, 2, 2, 3, 4, 4, 6, 8,8,9])
    #l = build_list_node([1, 1])
    print(l)
    print(Solution().deleteDuplicates(l))

