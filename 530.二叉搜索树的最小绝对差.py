#
# @lc app=leetcode.cn id=530 lang=python3
#
# [530] 二叉搜索树的最小绝对差
#
# https://leetcode-cn.com/problems/minimum-absolute-difference-in-bst/description/
#
# algorithms
# Easy (51.54%)
# Total Accepted:    3.2K
# Total Submissions: 6.1K
# Testcase Example:  '[1,null,3,2]'
#
# 给定一个所有节点为非负值的二叉搜索树，求树中任意两节点的差的绝对值的最小值。
#
# 示例 :
#
#
# 输入:
#
# ⁠  1
# ⁠   \
# ⁠    3
# ⁠   /
# ⁠  2
#
# 输出:
# 1
#
# 解释:
# 最小绝对差为1，其中 2 和 1 的差的绝对值为 1（或者 2 和 3）。
#
#
# 注意: 树中至少有2个节点。
#
#
# Definition for a binary tree node.

class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

# @lc code=start

class Solution(object):
    def getMinimumDifference(self, root: TreeNode) -> int:
        self.pre_val = None
        self.ans = float('inf')
        self.traverse(root)
        return self.ans

    def traverse(self, root: TreeNode):
        if not root:
            return
        self.traverse(root.left)
        if self.pre_val is not None:
            self.ans = min(self.ans, abs(root.val - self.pre_val))
        self.pre_val = root.val
        self.traverse(root.right)
# @lc code=end

if __name__ == "__main__":
    n1 = TreeNode(1)
    n2 = TreeNode(2)
    n3 = TreeNode(3)
    n4 = TreeNode(4)

    n1.right = n3
    n3.left = n2
    n3.right = n4
    n3.right = TreeNode(5)
    s = Solution().getMinimumDifference(n1)
    print(s)


