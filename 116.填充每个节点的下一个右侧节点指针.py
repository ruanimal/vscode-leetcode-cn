#
# @lc app=leetcode.cn id=116 lang=python3
#
# [116] 填充每个节点的下一个右侧节点指针
#
# https://leetcode-cn.com/problems/populating-next-right-pointers-in-each-node/description/
#
# algorithms
# Medium (71.16%)
# Likes:    700
# Dislikes: 0
# Total Accepted:    218.1K
# Total Submissions: 306.5K
# Testcase Example:  '[1,2,3,4,5,6,7]'
#
# 给定一个 完美二叉树 ，其所有叶子节点都在同一层，每个父节点都有两个子节点。二叉树定义如下：
#
#
# struct Node {
# ⁠ int val;
# ⁠ Node *left;
# ⁠ Node *right;
# ⁠ Node *next;
# }
#
# 填充它的每个 next 指针，让这个指针指向其下一个右侧节点。如果找不到下一个右侧节点，则将 next 指针设置为 NULL。
#
# 初始状态下，所有 next 指针都被设置为 NULL。
#
#
#
# 示例 1：
#
#
#
#
# 输入：root = [1,2,3,4,5,6,7]
# 输出：[1,#,2,3,#,4,5,6,7,#]
# 解释：给定二叉树如图 A 所示，你的函数应该填充它的每个 next 指针，以指向其下一个右侧节点，如图 B 所示。序列化的输出按层序遍历排列，同一层节点由
# next 指针连接，'#' 标志着每一层的结束。
#
#
#
#
# 示例 2:
#
#
# 输入：root = []
# 输出：[]
#
#
#
#
# 提示：
#
#
# 树中节点的数量在 [0, 2^12 - 1] 范围内
# -1000 <= node.val <= 1000
#
#
#
#
# 进阶：
#
#
# 你只能使用常量级额外空间。
# 使用递归解题也符合要求，本题中递归程序占用的栈空间不算做额外的空间复杂度。
#
#
#



from comm import *

# @lc code=start
class Node:
    def __init__(self, val: int = 0, left: 'Node' = None, right: 'Node' = None, next: 'Node' = None):
        self.val = val
        self.left = left
        self.right = right
        self.next = next

class Solution:
    def connect(self, root: 'Optional[Node]') -> 'Optional[Node]':
        """
        层级遍历(BFS),使用队列
        """

        if not root:
            return

        que = []
        que.append(root)
        while len(que) > 0:
            p = que[0]
            for i in que[1:]:
                p.next = i
                p = p.next
            next_que = []
            for i in que:
                if i.left:
                    next_que.append(i.left)
                if i.right:
                    next_que.append(i.right)
            que = next_que
        return root

class Solution_A:
    def connect(self, root: 'Optional[Node]') -> 'Optional[Node]':
        """
        递归解法, 实现简单
        比层级遍历法慢 200%
        """

        if root is None:
            return
        self.connectTowNode(root.left, root.right)
        return root

    def connectTowNode(self, node1, node2):
        if node1 is None or node2 is None:
            return
        node1.next = node2  # 前序位置
        self.connectTowNode(node1.left, node1.right)
        self.connectTowNode(node2.left, node2.right)
        self.connectTowNode(node1.right, node2.left)

# @lc code=end

