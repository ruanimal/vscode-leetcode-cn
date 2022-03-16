#
# @lc app=leetcode.cn id=297 lang=python3
#
# [297] 二叉树的序列化与反序列化
#
# https://leetcode-cn.com/problems/serialize-and-deserialize-binary-tree/description/
#
# algorithms
# Hard (56.92%)
# Likes:    786
# Dislikes: 0
# Total Accepted:    135.4K
# Total Submissions: 237.9K
# Testcase Example:  '[1,2,3,null,null,4,5]'
#
#
# 序列化是将一个数据结构或者对象转换为连续的比特位的操作，进而可以将转换后的数据存储在一个文件或者内存中，同时也可以通过网络传输到另一个计算机环境，采取相反方式重构得到原数据。
#
# 请设计一个算法来实现二叉树的序列化与反序列化。这里不限定你的序列 /
# 反序列化算法执行逻辑，你只需要保证一个二叉树可以被序列化为一个字符串并且将这个字符串反序列化为原始的树结构。
#
# 提示: 输入输出格式与 LeetCode 目前使用的方式一致，详情请参阅 LeetCode
# 序列化二叉树的格式。你并非必须采取这种方式，你也可以采用其他的方法解决这个问题。
#
#
#
# 示例 1：
#
#
# 输入：root = [1,2,3,null,null,4,5]
# 输出：[1,2,3,null,null,4,5]
#
#
# 示例 2：
#
#
# 输入：root = []
# 输出：[]
#
#
# 示例 3：
#
#
# 输入：root = [1]
# 输出：[1]
#
#
# 示例 4：
#
#
# 输入：root = [1,2]
# 输出：[1,2]
#
#
#
#
# 提示：
#
#
# 树中结点数在范围 [0, 10^4] 内
# -1000
#
#
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Codec_A:
    def serialize(self, root):
        """Encodes a tree to a single string.
        层次遍历
        :type root: TreeNode
        :rtype: str
        """
        if root is None:
            return '#'

        res = []
        que = [root]
        while que:
            new_que = []
            for n in que:
                if n is None:
                    res.append('#')
                else:
                    res.append(str(n.val))
                    new_que.append(n.left)
                    new_que.append(n.right)
            que = new_que
        return ','.join(res)


    def deserialize(self, data):
        """Decodes your encoded data to tree.

        :type data: str
        :rtype: TreeNode
        """
        if data == '#':
            return

        data = data.split(',')
        root = TreeNode(int(data[0]))
        que = [root]
        idx = 1
        while que:
            new_que = []
            for n in que:
                if data[idx] == '#':
                    n.left = None
                else:
                    n.left = TreeNode(int(data[idx]))
                    new_que.append(n.left)
                idx += 1
                if data[idx] == '#':
                    n.right = None
                else:
                    n.right = TreeNode(int(data[idx]))
                    new_que.append(n.right)
                idx += 1
            que = new_que
        return root


class Codec:
    def serialize(self, root):
        """Encodes a tree to a single string.
        前序遍历
        :type root: TreeNode
        :rtype: str
        """
        self.res = []
        self.serialize_helper(root)
        return ','.join(self.res)

    def serialize_helper(self, root):
        if root is None:
            self.res.append('')
            return
        self.res.append(str(root.val))
        self.serialize_helper(root.left)
        self.serialize_helper(root.right)

    def deserialize(self, data):
        """Decodes your encoded data to tree.

        :type data: str
        :rtype: TreeNode
        """
        if not data:
            return

        self.index = -1
        return self.deserialize_helper(data.split(','))

    def deserialize_helper(self, data):
        self.index += 1  # 注意增加的时机
        if data[self.index] == '':
            return

        root = TreeNode(int(data[self.index]))
        root.left = self.deserialize_helper(data)
        root.right = self.deserialize_helper(data)
        return root
# Your Codec object will be instantiated and called as such:
# ser = Codec()
# deser = Codec()
# ans = deser.deserialize(ser.serialize(root))
# @lc code=end

from comm import *
if __name__ == '__main__':
    pass

