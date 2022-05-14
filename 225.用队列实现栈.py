#
# @lc app=leetcode.cn id=225 lang=python3
#
# [225] 用队列实现栈
#
# https://leetcode-cn.com/problems/implement-stack-using-queues/description/
#
# algorithms
# Easy (54.98%)
# Total Accepted:    8.2K
# Total Submissions: 14.3K
# Testcase Example:  '["MyStack","push","push","top","pop","empty"]\n[[],[1],[2],[],[],[]]'
#
# 使用队列实现栈的下列操作：
#
#
# push(x) -- 元素 x 入栈
# pop() -- 移除栈顶元素
# top() -- 获取栈顶元素
# empty() -- 返回栈是否为空
#
#
# 注意:
#
#
# 你只能使用队列的基本操作-- 也就是 push to back, peek/pop from front, size, 和 is empty
# 这些操作是合法的。
# 你所使用的语言也许不支持队列。 你可以使用 list 或者 deque（双端队列）来模拟一个队列 , 只要是标准的队列操作即可。
# 你可以假设所有操作都是有效的（例如, 对一个空的栈不会调用 pop 或者 top 操作）。
#
#
#

from queue import Queue

class MyStack(object):

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.stack_q = Queue()
        self.tmp_q = Queue()

    def push(self, x: int):
        """
        Push element x onto stack.
        """
        self.stack_q.put(x)

    def pop(self) -> int:
        """
        Removes the element on top of the stack and returns that element.
        """
        if self.stack_q.empty():
            return

        tmp = None
        while not self.stack_q.empty():
            tmp = self.stack_q.get()
            if self.stack_q.empty():
                break
            self.tmp_q.put(tmp)
        self.stack_q, self.tmp_q = self.tmp_q, self.stack_q
        return tmp

    def top(self) -> int:
        """
        Get the top element.
        """
        if self.stack_q.empty():
            return

        t = self.pop()
        self.push(t)
        return t

    def empty(self) -> int:
        """
        Returns whether the stack is empty.
        """
        return self.stack_q.empty()


# Your MyStack object will be instantiated and called as such:
# obj = MyStack()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.top()
# param_4 = obj.empty()
if __name__ == "__main__":
    obj = MyStack()
    obj.push(1)
    obj.push(2)
    obj.push(3)
    print(obj.pop())
    print(obj.top())
    print(obj.empty())
