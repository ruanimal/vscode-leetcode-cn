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


def build(data):
    head = prev = None
    for i in data:
        node = ListNode(i)
        if prev:
            prev.next = node
        else:
            head = node
        prev = node
    return head

def reverse_list(head):
    cur, prev = head, None
    while cur:
        cur.next, prev, cur = prev, cur, cur.next
    return prev

def swap_pairs(head):
    result = ListNode(0)
    pre, pre.next = result, head
    while pre.next and pre.next.next:
        a = pre.next
        b = pre.next.next
        pre.next, b.next, a.next = b, a, b.next
        pre = a
    return result.next


head = build(range(10))
print(head)
print('+++')
print(swap_pairs(head))
