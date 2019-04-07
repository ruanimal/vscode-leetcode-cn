#
# @lc app=leetcode.cn id=707 lang=python
#
# [707] Design Linked List
#
# https://leetcode-cn.com/problems/design-linked-list/description/
#
# algorithms
# Easy (25.18%)
# Total Accepted:    5.6K
# Total Submissions: 21.5K
# Testcase Example:  '["MyLinkedList","addAtHead","addAtTail","addAtIndex","get","deleteAtIndex","get"]\n[[],[1],[3],[1,2],[1],[1],[1]]'
#
# 设计链表的实现。您可以选择使用单链表或双链表。单链表中的节点应该具有两个属性：val 和 next。val 是当前节点的值，next
# 是指向下一个节点的指针/引用。如果要使用双向链表，则还需要一个属性 prev 以指示链表中的上一个节点。假设链表中的所有节点都是 0-index 的。
#
# 在链表类中实现这些功能：
#
#
# get(index)：获取链表中第 index 个节点的值。如果索引无效，则返回-1。
# addAtHead(val)：在链表的第一个元素之前添加一个值为 val 的节点。插入后，新节点将成为链表的第一个节点。
# addAtTail(val)：将值为 val 的节点追加到链表的最后一个元素。
# addAtIndex(index,val)：在链表中的第 index 个节点之前添加值为 val  的节点。如果 index
# 等于链表的长度，则该节点将附加到链表的末尾。如果 index 大于链表长度，则不会插入节点。
# deleteAtIndex(index)：如果索引 index 有效，则删除链表中的第 index 个节点。
#
#
#
#
# 示例：
#
# MyLinkedList linkedList = new MyLinkedList();
# linkedList.addAtHead(1);
# linkedList.addAtTail(3);
# linkedList.addAtIndex(1,2);   //链表变为1-> 2-> 3
# linkedList.get(1);            //返回2
# linkedList.deleteAtIndex(1);  //现在链表是1-> 3
# linkedList.get(1);            //返回3
#
#
#
#
# 提示：
#
#
# 所有值都在 [1, 1000] 之内。
# 操作次数将在  [1, 1000] 之内。
# 请不要使用内置的 LinkedList 库。
#
#
#
class Node(object):
    def __init__(self, val):
        self.val = val
        self.next = None

    def __repr__(self):
        tmp = []
        node = self
        max_depth = 20
        while node:
            max_depth -= 1
            if max_depth < 0:
                break
            tmp.append('<{}>'.format(id(node)) + repr(node.val))
            node = node.next
        return ' -> '.join(tmp)

class MyLinkedList(object):

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.head = Node(-1)
        self.tail = self.head
        self.length = 0

    def get(self, index):
        """
        Get the value of the index-th node in the linked list. If the index is invalid, return -1.
        :type index: int
        :rtype: int
        """
        if index < 0 or index >= self.length:
            return -1

        p = self.head
        for i in range(index):
            p = p.next
        return p.val

    def addAtHead(self, val):
        """
        Add a node of value val before the first element of the linked list. After the insertion, the new node will be the first node of the linked list.
        :type val: int
        :rtype: None
        """
        t = Node(val)
        t.next = self.head
        self.head = t
        self.length += 1

    def addAtTail(self, val):
        """
        Append a node of value val to the last element of the linked list.
        :type val: int
        :rtype: None
        """
        self.tail.val = val
        self.tail.next = Node(-1)
        self.tail = self.tail.next
        self.length += 1

    def addAtIndex(self, index, val):
        """
        Add a node of value val before the index-th node in the linked list. If index equals to the length of linked list, the node will be appended to the end of linked list. If index is greater than the length, the node will not be inserted.
        :type index: int
        :type val: int
        :rtype: None
        """
        if index < 0 or index > self.length:
            return -1
        if index == 0:
            return self.addAtHead(val)

        p = self.head
        for i in range(index):
            p = p.next
        t = Node(p.val)
        t.next = p.next
        p.val = val
        p.next = t
        if p is self.tail:
            self.tail = self.tail.next
        self.length += 1

    def deleteAtIndex(self, index):
        """
        Delete the index-th node in the linked list, if the index is valid.
        :type index: int
        :rtype: None
        """
        if index < 0 or index >= self.length:
            return -1
        if index == 0 and self.length == 0:
            return
        p = self.head
        for i in range(index):
            p = p.next
        p.val = p.next.val
        p.next = p.next.next
        if p.next is None:
            self.tail = p
        self.length -= 1

if __name__ == "__main__":
    # ops = ["addAtHead","addAtTail","addAtIndex","get","deleteAtIndex","get"]
    # args = [[1],[3],[1,2],[1],[1],[1]]
    ops = ["addAtHead","addAtIndex","get","get","get"]
    args = [[1],[1,2],[1],[0],[2]]

    obj = MyLinkedList()

    for op, arg in zip(ops, args):
        x = getattr(obj, op)(*arg)
        print(op, arg, obj.head, obj.tail, obj.length)
        print(repr(x))
        # if op == 'addAtTail' and arg == [1]:
        #     import ipdb; ipdb.set_trace()
        #     print(op, arg, obj.head)
        #     print(repr(x))

#   ✘ answer: [null,null,null,null,-1,null,-1]
#   ✘ expected_answer: [null,null,null,null,2,null,3]
