class Node(object):
    def __init__(self, val=None):
        self.val = val
        self.left = None
        self.right = None

    def __repr__(self):
        return 'Node({})'.format(self.val)

def build(elements):
    root = Node(elements[0] if elements else None)
    level = [root]
    i = 1
    while i < len(elements):
        next_level = []
        for node in level:
            if i >= len(elements): break
            node.left = Node(elements[i])
            next_level.append(node.left)
            i += 1
            if i >= len(elements): break
            node.right = Node(elements[i])
            i += 1
            next_level.append(node.right)
        level = next_level
    return root


def print_tree(root):
    level = [root]
    ans = []
    while level:
        ans.append([str(i.val) if i.val is not None else 'n'  for i in level])
        next_level = []
        for node in level:
            if node.left:
                next_level.append(node.left)
            if node.right:
                next_level.append(node.right)
        level = next_level

    strings = []
    item_width = 2
    width = 2 ** len(ans) * 2 * item_width
    pading = ' ' * item_width
    for level in range(len(ans)-1, -1, -1):
        i = ['{:^2}'.format(xx) for xx in ans[level]]
        partern = '{:^%s}' % (width)
        raw_line = pading.join(i)
        if level == (len(ans)-1):
            raw_line += ((2 ** (level+1)-1) * item_width - len(raw_line)) * ' '
        # print(repr(raw_line))
        line = partern.format(raw_line)
        strings.append(line)
        pading = ' ' * ((len(pading) + item_width) * 2 - item_width)
    for i in strings[::-1]:
        print(i)


def pre_order_traversal(root):
    """前序遍历"""
    if not root.right and not root.left:
        return [root.val]

    left = pre_order_traversal(root.left) if root.left else []
    right = pre_order_traversal(root.right) if root.right else []
    return [root.val] + left + right

def pre_order_traversal_2(root):
    """前序遍历"""
    ans = []
    stack = []
    node = root
    while node or stack:
        while node:
            ans.append(node.val)
            stack.append(node)
            node = node.left
        node = stack.pop()
        node = node.right
    return ans

def pre_order_traversal_3(root):
    """前序遍历"""
    if not root:
        return []

    ans = []
    stack = [(1, root)]
    while stack:
        state, node = stack.pop()
        if state == 0:
            ans.append(node.val)
            continue

        if node.right:
            stack.append((1, node.right))
        if node.left:
            stack.append((1, node.left))
        stack.append((0, node))
    return ans

def in_order_traversal(root):
    """中序遍历"""
    if not root.right and not root.left:
        return [root.val]

    left = in_order_traversal(root.left) if root.left else []
    right = in_order_traversal(root.right) if root.right else []
    return left + [root.val] + right


def in_order_traversal_2(root):
    """中序遍历"""
    ans = []
    stack = []
    node = root
    while node or stack:
        while node:
            stack.append(node)
            node = node.left
        node = stack.pop()
        ans.append(node.val)
        node = node.right
    return ans


def in_order_traversal_3(root):
    """中序遍历"""
    if not root:
        return []

    ans = []
    stack = [(1, root)]
    while stack:
        state, node = stack.pop()
        if state == 0:
            ans.append(node.val)
            continue

        if node.right:
            stack.append((1, node.right))
        stack.append((0, node))
        if node.left:
            stack.append((1, node.left))
    return ans

def post_order_traversal(root):
    """前序遍历"""
    if not root.right and not root.left:
        return [root.val]

    left = post_order_traversal(root.left) if root.left else []
    right = post_order_traversal(root.right) if root.right else []
    return left + right + [root.val]


def post_order_traversal_2(root):
    """后序遍历"""
    ans = []
    stack1 = []
    stack2 = []
    stack1.append(root)
    while stack1:   # 找出后序遍历的逆序，存放在 stack2中
        node = stack1.pop()
        if node.left:
            stack1.append(node.left)
        if node.right:
            stack1.append(node.right)
        stack2.append(node)
    while stack2:  # 将 stack2中的元素出栈，即是后序遍历序列
        ans.append(stack2.pop().val)
    return ans


def post_order_traversal_3(root):
    """后序遍历"""
    if not root:
        return []

    ans = []
    stack = [(1, root)]
    while stack:
        state, node = stack.pop()
        if state == 0:
            ans.append(node.val)
            continue

        stack.append((0, node))
        if node.right:
            stack.append((1, node.right))
        if node.left:
            stack.append((1, node.left))
    return ans

def level_traversal(root):
    level = [root]
    ans = []
    while level:
        next_level = []
        for node in level:
            ans.append(node.val)
            if node.left:
                next_level.append(node.left)
            if node.right:
                next_level.append(node.right)
        level = next_level
    return ans

if __name__ == "__main__":
    tree = build(list(range(14)))
    print_tree(tree)
    # print(pre_order_traversal(tree))
    # print(pre_order_traversal_2(tree))
    # print(pre_order_traversal_3(tree))
    # print(in_order_traversal(tree))
    # print(in_order_traversal_2(tree))
    # print(in_order_traversal_3(tree))
    print(post_order_traversal(tree))
    print(post_order_traversal_2(tree))
    print(post_order_traversal_3(tree))
    # print(level_traversal(tree))
