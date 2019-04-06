#
# @lc app=leetcode.cn id=559 lang=python
#
# [559] Maximum Depth of N-ary Tree
#
# https://leetcode-cn.com/problems/maximum-depth-of-n-ary-tree/description/
#
# algorithms
# Easy (64.19%)
# Total Accepted:    5.5K
# Total Submissions: 8.5K
# Testcase Example:  '{"$id":"1","children":[{"$id":"2","children":[{"$id":"5","children":[],"val":5},{"$id":"6","children":[],"val":6}],"val":3},{"$id":"3","children":[],"val":2},{"$id":"4","children":[],"val":4}],"val":1}'
#
# 给定一个 N 叉树，找到其最大深度。
#
# 最大深度是指从根节点到最远叶子节点的最长路径上的节点总数。
#
# 例如，给定一个 3叉树 :
#
#
#
#
#
#
#
# 我们应返回其最大深度，3。
#
# 说明:
#
#
# 树的深度不会超过 1000。
# 树的节点总不会超过 5000。
#
#
"""
# Definition for a Node.
class Node(object):
    def __init__(self, val, children):
        self.val = val
        self.children = children
"""
class Node(object):
    def __init__(self, val, children):
        self.val = val
        self.children = children

    def __repr__(self):
        return 'Node(%r, %r)' % (self.val, self.children)

class Solution(object):
    def maxDepth1(self, root):
        """
        :type root: Node
        :rtype: int
        """
        def dfs(node):
            print('+')
            if not node.children:
                max_depth[0] = max(max_depth[0], len(tmp))
                return

            for i in node.children:
                tmp.append(i)
                dfs(i)
                tmp.pop()

        if not root:
            return 0

        max_depth = [0]
        tmp = [root]
        dfs(root)
        return max_depth[0]

    def maxDepth(self, root):
        """
        :type root: Node
        :rtype: int
        """
        print('=')
        if not root:
            return 0

        max_depth = 1
        for i in root.children:
            max_depth = max(max_depth, 1 + self.maxDepth(i))
        return max_depth

if __name__ == "__main__":
    n1 = Node(1, [Node(2, []), Node(3, [Node(4, [])])])
    root = Node(0, [n1])
    s = Solution().maxDepth(root)
    print(s)
    s = Solution().maxDepth1(root)
    print(s)

