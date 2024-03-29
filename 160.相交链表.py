#
# @lc app=leetcode.cn id=160 lang=python3
#
# [160] 相交链表
#
# https://leetcode-cn.com/problems/intersection-of-two-linked-lists/description/
#
# algorithms
# Easy (35.50%)
# Total Accepted:    19.2K
# Total Submissions: 49.9K
# Testcase Example:  '8\n[4,1,8,4,5]\n[5,0,1,8,4,5]\n2\n3'
#
# 编写一个程序，找到两个单链表相交的起始节点。
#
# 如下面的两个链表：
#
#
#
# 在节点 c1 开始相交。
#
#
#
# 示例 1：
#
#
#
# 输入：intersectVal = 8, listA = [4,1,8,4,5], listB = [5,0,1,8,4,5], skipA = 2,
# skipB = 3
# 输出：Reference of the node with value = 8
# 输入解释：相交节点的值为 8 （注意，如果两个列表相交则不能为 0）。从各自的表头开始算起，链表 A 为 [4,1,8,4,5]，链表 B 为
# [5,0,1,8,4,5]。在 A 中，相交节点前有 2 个节点；在 B 中，相交节点前有 3 个节点。
#
#
#
#
# 示例 2：
#
#
#
# 输入：intersectVal = 2, listA = [0,9,1,2,4], listB = [3,2,4], skipA = 3, skipB =
# 1
# 输出：Reference of the node with value = 2
# 输入解释：相交节点的值为 2 （注意，如果两个列表相交则不能为 0）。从各自的表头开始算起，链表 A 为 [0,9,1,2,4]，链表 B 为
# [3,2,4]。在 A 中，相交节点前有 3 个节点；在 B 中，相交节点前有 1 个节点。
#
#
#
#
# 示例 3：
#
#
#
# 输入：intersectVal = 0, listA = [2,6,4], listB = [1,5], skipA = 3, skipB = 2
# 输出：null
# 输入解释：从各自的表头开始算起，链表 A 为 [2,6,4]，链表 B 为 [1,5]。由于这两个链表不相交，所以 intersectVal 必须为
# 0，而 skipA 和 skipB 可以是任意值。
# 解释：这两个链表不相交，因此返回 null。
#
#
#
#
# 注意：
#
#
# 如果两个链表没有交点，返回 null.
# 在返回结果后，两个链表仍须保持原有的结构。
# 可假定整个链表结构中没有循环。
# 程序尽量满足 O(n) 时间复杂度，且仅用 O(1) 内存。
#
#
#
# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None


from comm import *

# @lc code=start

class Solution_A(object):
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> ListNode:
        """
        遍历一次链表, 记录两个链表的长度, a, b
        用两个指针, 让长的链表先走 abs(a-b)步, 然后两个指针同时遍历, 指针相等时, 值就为链表交点
        """

        if not (headA and headB):
            return
        if headA == headB:
            return headA
        if headA.next == headB.next:
            return headA.next

        count1 = 0
        count2 = 0
        p1 = headA
        p2 = headB

        while p1.next:
            count1 += 1
            p1 = p1.next
        while p2.next:
            count2 += 1
            p2 = p2.next
        if p1 != p2:
            return

        p1 = headA
        p2 = headB
        while count1 > count2:
            p1 = p1.next
            count1 -= 1
        while count1 < count2:
            p2 = p2.next
            count2 -= 1
        while p1 and p2:
            if p1 == p2:
                return p1
            else:
                p1 = p1.next
                p2 = p2.next

class Solution_B(object):
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> ListNode:
        """
        将A链的末尾链上B链的头部, 转化为求链表环的问题
        """
        if not headA or not headB:
            return

        p = headA
        while p.next:
            p = p.next
        p.next = headB   # 链表相连
        slow = fast = headA
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
            if slow == fast:
                break
        if fast is None or fast.next is None:   # 无环
            p.next = None  # 还原相连的链表
            return
        slow = headA
        while slow != fast:
            slow = slow.next
            fast = fast.next
        p.next = None  # 还原相连的链表
        return slow

class Solution(object):
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> ListNode:
        """
        A: A单独部分
        B: B单独部分
        C: 相交的部分

        则:
            p1 = A + C + B + C
            p2 = B + C + A + C
            p1 == p2

        还得排除C长度为0的情况, 也就是没有相交
        """

        if not headA or not headB:
            return

        p1, p2 = headA, headB
        while p1 != p2:   # 结束时, 两者都为None, 或者两者相等
            if p1 is None:
                p1 = headB
            else:
                p1 = p1.next
            if p2 is None:
                p2 = headA
            else:
                p2 = p2.next
        return p1

# @lc code=end

