#
# @lc app=leetcode.cn id=897 lang=python
#
# [897] 递增顺序查找树
#
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def increasingBST(self, root, tail=None):
        """
        :type root: TreeNode
        :rtype: TreeNode
        """
        # 纯递归解法, 比较难理解
        # if not root:
        #     return tail
        # r = self.increasingBST(root.left, root)
        # root.left = None
        # root.right = self.increasingBST(root.right, tail)
        # return r

        def mid_dfs(node, ret=None):
            if ret is None:
                ret = []
            if not node:
                return
            mid_dfs(node.left, ret)
            node.left = None
            ret.append(node)
            mid_dfs(node.right, ret)
            return ret
        ret = mid_dfs(root)
        ret[-1].right = None   # 去除旧的右节点
        ans = ret[0]
        for i in range(len(ret)-1):
            ret[i].right = ret[i+1]
        return ans

