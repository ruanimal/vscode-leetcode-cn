#
# @lc app=leetcode.cn id=109 lang=python3
#
# [109] 有序链表转换二叉搜索树
#
# https://leetcode.cn/problems/convert-sorted-list-to-binary-search-tree/description/
#
# algorithms
# Medium (76.94%)
# Likes:    939
# Dislikes: 0
# Total Accepted:    173.6K
# Total Submissions: 225.6K
# Testcase Example:  '[-10,-3,0,5,9]'
#
# 给定一个单链表的头节点  head ，其中的元素 按升序排序 ，将其转换为 平衡 二叉搜索树。
#
#
#
# 示例 1:
#
#
#
#
# 输入: head = [-10,-3,0,5,9]
# 输出: [0,-3,9,-10,null,5]
# 解释: 一个可能的答案是[0，-3,9，-10,null,5]，它表示所示的高度平衡的二叉搜索树。
#
#
# 示例 2:
#
#
# 输入: head = []
# 输出: []
#
#
#
#
# 提示:
#
#
# head 中的节点数在[0, 2 * 10^4] 范围内
# -10^5 <= Node.val <= 10^5
#
#
#

from comm import *
# @lc code=start
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

T = Optional[ListNode]

class Solution:
    def sortedListToBST(self, head: T, right: T=None) -> Optional[TreeNode]:
        if head == right:
            return
        fast = slow = head
        while fast != right and fast.next != right:
            slow = slow.next
            fast = fast.next.next
        root = TreeNode(slow.val)
        root.left = self.sortedListToBST(head, slow)
        root.right = self.sortedListToBST(slow.next, right)
        return root
# @lc code=end

l = build_list_node([-10,-3,0,5,9])

s = Solution().sortedListToBST(l)
print(s)
