#
# @lc app=leetcode.cn id=234 lang=python3
#
# [234] 回文链表
#
# https://leetcode-cn.com/problems/palindrome-linked-list/description/
#
# algorithms
# Easy (34.89%)
# Total Accepted:    18.3K
# Total Submissions: 51.3K
# Testcase Example:  '[1,2]'
#
# 请判断一个链表是否为回文链表。
#
# 示例 1:
#
# 输入: 1->2
# 输出: false
#
# 示例 2:
#
# 输入: 1->2->2->1
# 输出: true
#
#
# 进阶：
# 你能否用 O(n) 时间复杂度和 O(1) 空间复杂度解决此题？

from comm import *

# @lc code=start


class Solution(object):
    def isPalindrome(self, head: ListNode) -> bool:
        """
        快慢指针法, 反转其中一半, 比较
        """
        if not head:
            return True
        if not head.next:
            return True

        fast_ptr = slow_ptr = head
        while fast_ptr.next and fast_ptr.next.next:
            slow_ptr = slow_ptr.next
            fast_ptr = fast_ptr.next.next

        head_b = slow_ptr.next
        slow_ptr.next = None

        new_head = ListNode(None)
        new_head.next = ptr = head_b
        while ptr.next:
            tmp = ptr.next
            ptr.next = ptr.next.next
            tmp.next = new_head.next
            new_head.next = tmp

        ptr_a = head
        ptr_b = new_head.next
        while ptr_b:
            if ptr_a.val != ptr_b.val:
                return False
            ptr_a = ptr_a.next
            ptr_b = ptr_b.next
        return True

class SolutionA(object):
    def traverse(self, right):
        """判断左右往里各移动移动一位之后是不是回文
        性能比较差, 耗时为迭代法的2倍, 适合用来理解递归

        后序遍历
        """
        if not right:
            return True
        res = self.traverse(right.next)
        res = res and right.val == self.left.val
        self.left = self.left.next
        return res

    def isPalindrome(self, head: ListNode) -> bool:
        """
        递归法
        """
        if not head:
            return

        self.left = head
        return self.traverse(head)

# @lc code=end
