#
# @lc app=leetcode.cn id=99 lang=python3
#
# [99] 恢复二叉搜索树
#
# https://leetcode.cn/problems/recover-binary-search-tree/description/
#
# algorithms
# Medium (61.24%)
# Likes:    994
# Dislikes: 0
# Total Accepted:    165.7K
# Total Submissions: 270.5K
# Testcase Example:  '[1,3,null,null,2]'
#
# 给你二叉搜索树的根节点 root ，该树中的 恰好 两个节点的值被错误地交换。请在不改变其结构的情况下，恢复这棵树 。
#
#
#
# 示例 1：
#
#
# 输入：root = [1,3,null,null,2]
# 输出：[3,1,null,null,2]
# 解释：3 不能是 1 的左孩子，因为 3 > 1 。交换 1 和 3 使二叉搜索树有效。
#
#
# 示例 2：
#
#
# 输入：root = [3,1,4,null,null,2]
# 输出：[2,1,4,null,null,3]
# 解释：2 不能在 3 的右子树中，因为 2 < 3 。交换 2 和 3 使二叉搜索树有效。
#
#
#
# 提示：
#
#
# 树上节点的数目在范围 [2, 1000] 内
# -2^31 <= Node.val <= 2^31 - 1
#
#
#
#
# 进阶：使用 O(n) 空间复杂度的解法很容易实现。你能想出一个只使用 O(1) 空间的解决方案吗？
#
#

from comm import *
# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

T = Optional[TreeNode]

class SolutionA:
    def helper(self, root: T, nodes: List[TreeNode]):
        if not root:
            return
        self.helper(root.left, nodes)
        nodes.append(root)
        self.helper(root.right, nodes)

    def recoverTree(self, root: T) -> None:
        """
        利用中序排序的性质
        """
        nodes: List[TreeNode] = []
        self.helper(root, nodes)
        l = 0
        r = len(nodes)-1
        while l < r:
            if nodes[l].val < nodes[l+1].val:
                l += 1
            elif nodes[r].val > nodes[r-1].val:
                r -= 1
            else:
                nodes[l].val, nodes[r].val = nodes[r].val, nodes[l].val
                break
        return root

class Solution:
    def recoverTree(self, root: T) -> None:
        def dfs(root: T):
            if not root:
                return
            dfs(root.left)
            if self.pre is None:
                self.pre = root
            else:
                if root.val < self.pre.val:
                    if not self.x:   # x,y相邻
                        self.x = self.pre
                        self.y = root
                    else:    # x,y不相邻
                        self.y = root
                self.pre = root
            dfs(root.right)

        self.pre = self.x = self.y = None
        dfs(root)
        print(repr(self.x), repr(self.y))
        if self.x and self.y:
            self.x.val, self.y.val =  self.y.val, self.x.val

# @lc code=end

null = None
values = [1,6,3,4,5,2,7,8]  # None表示空节点
root = build_tree(values)
print(root)
Solution().recoverTree(root)
print(root)
