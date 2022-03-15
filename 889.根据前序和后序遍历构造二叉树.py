#
# @lc app=leetcode.cn id=889 lang=python3
#
# [889] 根据前序和后序遍历构造二叉树
#
# https://leetcode-cn.com/problems/construct-binary-tree-from-preorder-and-postorder-traversal/description/
#
# algorithms
# Medium (67.56%)
# Likes:    230
# Dislikes: 0
# Total Accepted:    20.5K
# Total Submissions: 30.4K
# Testcase Example:  '[1,2,4,5,3,6,7]\n[4,5,2,6,7,3,1]'
#
# 给定两个整数数组，preorder 和 postorder ，其中 preorder 是一个具有 无重复 值的二叉树的前序遍历，postorder
# 是同一棵树的后序遍历，重构并返回二叉树。
#
# 如果存在多个答案，您可以返回其中 任何 一个。
#
#
#
# 示例 1：
#
#
#
#
# 输入：preorder = [1,2,4,5,3,6,7], postorder = [4,5,2,6,7,3,1]
# 输出：[1,2,3,4,5,6,7]
#
#
# 示例 2:
#
#
# 输入: preorder = [1], postorder = [1]
# 输出: [1]
#
#
#
#
# 提示：
#
#
# 1 <= preorder.length <= 30
# 1 <= preorder[i] <= preorder.length
# preorder 中所有值都 不同
# postorder.length == preorder.length
# 1 <= postorder[i] <= postorder.length
# postorder 中所有值都 不同
# 保证 preorder 和 postorder 是同一棵二叉树的前序遍历和后序遍历
#
#
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

try:
    from comm import *
except ImportError:
    LOCAL_TEST = False

class Solution:
    def constructFromPrePost(self, preorder: List[int], postorder: List[int]) -> TreeNode:
        if len(preorder) == 0 or len(postorder) == 0:
            return

        self.postorder_index = {i[1]:i[0] for i in enumerate(postorder)}
        self.preorder_index = {i[1]:i[0] for i in enumerate(preorder)}
        return self.helper(preorder, postorder, 0, len(preorder)-1, 0, len(postorder)-1)

    def helper(self, preorder: List[int], postorder: List[int],
               pre_low, pre_high, post_low, post_high) -> TreeNode:
        # pre_low, pre_high => 子树在前序数组的位置 => 该子树的前序数组
        # post_low, post_high => 子树在后序数组的位置 => 该子树的后序数组
        if (pre_high - pre_low < 0):   # 一侧子树为空的情况
            return
        if pre_low == pre_high:
            return TreeNode(preorder[pre_low])   # 叶子节点

        lroot_val = preorder[pre_low+1]
        rroot_val = postorder[post_high-1]
        root = TreeNode(preorder[pre_low])
        # 通过后序数组得到左子树的右边界
        root.left = self.helper(preorder, postorder,
                                pre_low+1, self.preorder_index[rroot_val]-1,
                                post_low, self.postorder_index[lroot_val])
        # 通过前序数组得到右子树的左边界
        root.right = self.helper(preorder, postorder,
                                 self.preorder_index[rroot_val], pre_high,
                                 self.preorder_index[rroot_val]+1, post_high-1)
        return root

if LOCAL_TEST:
    s = Solution()
    s.constructFromPrePost(preorder = [1,2,4,5,3,6,7], postorder = [4,5,2,6,7,3,1])


# @lc code=end

