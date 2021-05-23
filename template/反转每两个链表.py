class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

    def __repr__(self):
        tmp = []
        node = self
        max_depth = 20
        while node:
            max_depth -= 1
            if max_depth < 0:
                break
            tmp.append(repr(node.val))
            node = node.next
        else:
            tmp.append('None')
        return ' -> '.join(tmp)


def build_list_node(nums):
    head = node = ListNode(None)
    for i in nums:
        node.next = ListNode(i)
        node = node.next
    return head.next


def swap_pairs(head):
    pre = None
    result = ListNode(0)
    pre, pre.next = result, head
    while pre.next and pre.next.next:
        a = pre.next
        b = pre.next.next
        pre.next, b.next, a.next = b, a, b.next
        pre = a
    return result.next


l = build_list_node(range(1, 10))

print(swap_pairs(l))
