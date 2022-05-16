#
# @lc app=leetcode.cn id=328 lang=python3
#
# [328] 奇偶链表
#
# https://leetcode-cn.com/problems/odd-even-linked-list/description/
#
# algorithms
# Medium (53.69%)
# Total Accepted:    7.7K
# Total Submissions: 14K
# Testcase Example:  '[1,2,3,4,5]'
#
# 给定一个单链表，把所有的奇数节点和偶数节点分别排在一起。请注意，这里的奇数节点和偶数节点指的是节点编号的奇偶性，而不是节点的值的奇偶性。
#
# 请尝试使用原地算法完成。你的算法的空间复杂度应为 O(1)，时间复杂度应为 O(nodes)，nodes 为节点总数。
#
# 示例 1:
#
# 输入: 1->2->3->4->5->NULL
# 输出: 1->3->5->2->4->NULL
#
#
# 示例 2:
#
# 输入: 2->1->3->5->6->4->7->NULL
# 输出: 2->3->6->7->1->5->4->NULL
#
# 说明:
#
#
# 应当保持奇数节点和偶数节点的相对顺序。
# 链表的第一个节点视为奇数节点，第二个节点视为偶数节点，以此类推。

from comm import *
# @lc code=start


class Solution(object):
    def oddEvenList(self, head: ListNode) -> ListNode:
        """
        使用dummyhead, 将偶数节点逐个取下, 练到新偶数链表末尾

        将新偶数链表连到原链表末尾
        """
        if not head or not head.next or not head.next.next:
            return head
        new_head = ListNode(None)
        ptr = head
        ptr2 = new_head
        while ptr and ptr.next:
            tmp = ptr.next
            ptr.next = ptr.next.next
            ptr2.next = tmp
            if ptr.next:
                ptr = ptr.next
            ptr2 = ptr2.next
        ptr2.next = None
        ptr.next = new_head.next
        return head

# @lc code=end

if __name__ == "__main__":
    l = build_list_node(range(1, 10))
    print(Solution().oddEvenList(l))
