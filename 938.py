
class Solution(object):
    def rangeSumBST(self, root, L, R):
        """
        :type root: TreeNode
        :type L: int
        :type R: int
        :rtype: int
        """
        if not root:
            return 0
        res = 0
        if L <= root.val <= R:
            res += root.val
        if root.val > L:
            res += self.rangeSumBST(root.left, L, R)
        if root.val < R:
            res += self.rangeSumBST(root.right, L, R)
        return res
