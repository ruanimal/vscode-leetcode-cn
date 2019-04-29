#
# @lc app=leetcode.cn id=108 lang=python
#
# [108] 将有序数组转换为二叉搜索树
#
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def sortedArrayToBST(self, nums):
        """
        :type nums: List[int]
        :rtype: TreeNode
        """
        # # 比较慢， 存在对象的复制
        # if not nums:
        #     return
        # mid = len(nums) // 2
        # node = TreeNode(nums[mid])
        # node.left = self.sortedArrayToBST(nums[:mid])
        # node.right = self.sortedArrayToBST(nums[mid+1:])
        # return node

        # 原以为这个版本比较快， 其实没啥差别
        def to_bst(nums, start, end):
            if start > end:
                return None
            mid = (start+end)//2
            node = TreeNode(nums[mid])
            node.left = to_bst(nums, start, mid-1)
            node.right = to_bst(nums, mid+1,end)
            return node
        return to_bst(nums, 0, len(nums) - 1)

