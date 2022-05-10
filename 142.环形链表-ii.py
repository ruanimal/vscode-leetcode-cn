#
# @lc app=leetcode.cn id=142 lang=python3
#
# [142] 环形链表 II
#
# https://leetcode-cn.com/problems/linked-list-cycle-ii/description/
#
# algorithms
# Medium (55.77%)
# Likes:    1446
# Dislikes: 0
# Total Accepted:    388.3K
# Total Submissions: 696.2K
# Testcase Example:  '[3,2,0,-4]\n1'
#
# 给定一个链表的头节点  head ，返回链表开始入环的第一个节点。 如果链表无环，则返回 null。
#
# 如果链表中有某个节点，可以通过连续跟踪 next 指针再次到达，则链表中存在环。 为了表示给定链表中的环，评测系统内部使用整数 pos
# 来表示链表尾连接到链表中的位置（索引从 0 开始）。如果 pos 是 -1，则在该链表中没有环。注意：pos
# 不作为参数进行传递，仅仅是为了标识链表的实际情况。
#
# 不允许修改 链表。
#
#
#
#
#
#
# 示例 1：
#
#
#
#
# 输入：head = [3,2,0,-4], pos = 1
# 输出：返回索引为 1 的链表节点
# 解释：链表中有一个环，其尾部连接到第二个节点。
#
#
# 示例 2：
#
#
#
#
# 输入：head = [1,2], pos = 0
# 输出：返回索引为 0 的链表节点
# 解释：链表中有一个环，其尾部连接到第一个节点。
#
#
# 示例 3：
#
#
#
#
# 输入：head = [1], pos = -1
# 输出：返回 null
# 解释：链表中没有环。
#
#
#
#
# 提示：
#
#
# 链表中节点的数目范围在范围 [0, 10^4] 内
# -10^5 <= Node.val <= 10^5
# pos 的值为 -1 或者链表中的一个有效索引
#
#
#
#
# 进阶：你是否可以使用 O(1) 空间解决此题？
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
    def detectCycle(self, head: ListNode) -> ListNode:
        """
        K: N倍环长(等价于一个大环)
        X: 环起点距离
        Y: 相遇位置距离环起点距离
        K - Y: 另一半环
        X + Y: p1移动距离
        X + Y + K: p2移动距离
        所以:
            2(X + Y) = X + Y + K
               X + Y = K
                   X = K - Y

        也就是: 环起点距离 = 另一半环
        那么从'起点'和'相遇点', 同时出发, 再次相遇的时候刚好就是环起点
        """

        if not head or not head.next:
            return

        p1 = p2 = head
        while p2 and p2.next:
            p2 = p2.next.next
            p1 = p1.next
            if p1 == p2:
                break
        if p2 is None or p2.next is None:  # 到达末尾
            return

        p1 = head
        while p1 != p2:
            p1 = p1.next
            p2 = p2.next
        return p1

# @lc code=end
