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


def reverse_link_list(head):
    cur, prev = head, None
    while cur:
        cur.next, prev, cur = prev, cur, cur.next
        # a = cur.next
        # b = prev
        # c = cur
        # cur.next = b
        # prev = c
        # cur = a
    return prev


l = build_list_node(range(1, 10))

print(reverse_link_list(l))
