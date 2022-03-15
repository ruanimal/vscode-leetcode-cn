#
# @lc app=leetcode.cn id=105 lang=python3
#
# [105] 从前序与中序遍历序列构造二叉树
#
# https://leetcode-cn.com/problems/construct-binary-tree-from-preorder-and-inorder-traversal/description/
#
# algorithms
# Medium (70.85%)
# Likes:    1481
# Dislikes: 0
# Total Accepted:    316.7K
# Total Submissions: 447K
# Testcase Example:  '[3,9,20,15,7]\n[9,3,15,20,7]'
#
# 给定两个整数数组 preorder 和 inorder ，其中 preorder 是二叉树的先序遍历， inorder
# 是同一棵树的中序遍历，请构造二叉树并返回其根节点。
#
#
#
# 示例 1:
#
#
# 输入: preorder = [3,9,20,15,7], inorder = [9,3,15,20,7]
# 输出: [3,9,20,null,null,15,7]
#
#
# 示例 2:
#
#
# 输入: preorder = [-1], inorder = [-1]
# 输出: [-1]
#
#
#
#
# 提示:
#
#
# 1 <= preorder.length <= 3000
# inorder.length == preorder.length
# -3000 <= preorder[i], inorder[i] <= 3000
# preorder 和 inorder 均 无重复 元素
# inorder 均出现在 preorder
# preorder 保证 为二叉树的前序遍历序列
# inorder 保证 为二叉树的中序遍历序列
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
    def buildTree(self, preorder: List[int], inorder: List[int]) -> TreeNode:
        """
        参考[654] 最大二叉树, 不过是根节点由前序数组提供
        """

        if len(preorder) == 0 or len(inorder) == 0:
            return

        self.call_index = -1
        self.inorder_index = {i[1]:i[0] for i in enumerate(inorder)}
        return self.helper(preorder, inorder, 0, len(inorder)-1)

    def helper(self, preorder: List[int], inorder: List[int], left, right) -> TreeNode:
        if (right-left) < 0:
            return

        self.call_index += 1
        # 前序遍历的顺序也就是中序遍历中根节点出现的顺序
        idx = self.inorder_index[preorder[self.call_index]]
        root = TreeNode(inorder[idx])
        root.left = self.helper(preorder, inorder, left, idx-1)
        root.right = self.helper(preorder, inorder, idx+1, right)
        return root

if LOCAL_TEST:
    s = Solution()
    print(s.buildTree([3,9,20,15,7], [9,3,15,20,7]))

# @lc code=end

