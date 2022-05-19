#
# @lc app=leetcode.cn id=429 lang=python3
#
# [429] N-ary Tree Level Order Traversal
#
# https://leetcode-cn.com/problems/n-ary-tree-level-order-traversal/description/
#
# algorithms
# Easy (58.66%)
# Total Accepted:    4.3K
# Total Submissions: 7.3K
# Testcase Example:  '{"$id":"1","children":[{"$id":"2","children":[{"$id":"5","children":[],"val":5},{"$id":"6","children":[],"val":6}],"val":3},{"$id":"3","children":[],"val":2},{"$id":"4","children":[],"val":4}],"val":1}'
#
# 给定一个 N 叉树，返回其节点值的层序遍历。 (即从左到右，逐层遍历)。
#
# 例如，给定一个 3叉树 :
#
#
#
#
#
#
#
# 返回其层序遍历:
#
# [
# ⁠    [1],
# ⁠    [3,2,4],
# ⁠    [5,6]
# ]
#
#
#
#
# 说明:
#
#
# 树的深度不会超过 1000。
# 树的节点总数不会超过 5000。
#
#

from comm import *
# @lc code=start

class Node:
    def __init__(self, val, children):
        self.val = val
        self.children = children

class Solution:
    def levelOrder(self, root: Node) -> List[List[int]]:
        if not root:
            return []

        ret = [[root.val]]
        level = [root]
        while level:
            next_level = []
            for node in level:
                next_level.extend(node.children)
            if next_level:
                ret.append([i.val for i in next_level])
            level = next_level
        return ret

# @lc code=end

if __name__ == "__main__":
    n1 = Node(1, [Node(2, []), Node(3, [Node(4, [])])])
    root = Node(0, [n1])
    s = Solution().levelOrder(root)
    print(s)



