class Node(object):
    def __init__(self, key, val, n):
        self.key = key
        self.val = val
        self.left = None
        self.right = None
        self.n = n  # 节点总数

    def __repr__(self):
        return '%s<%r:%r, %s>' % (self.__class__.__name__, self.key, self.val, self.n)

class BinarySearchTree:
    def __init__(self):
        self._root = None

    def size(self, node):
        if node is None:
            return 0
        return node.n

    @staticmethod
    def _get(node, key):
        if node is None:
            return
        if key < node.key:
            return BinarySearchTree._get(node.left, key)
        elif key > node.key:
            return BinarySearchTree._get(node.right, key)
        else:
            return node.val

    def get(self, key=None):
        if key is None:
            return
        return self._get(self._root, key)

    def _put(self, node, key, val):
        if node is None:   # 叶节点
            return Node(key, val, 1)
        if key < node.key:
            node.left = self._put(node.left, key, val)
        elif key > node.key:
            node.right = self._put(node.right, key, val)
        else:
            node.val = val
        node.n = self.size(node.left) + self.size(node.right) + 1
        return node

    def put(self, key=None, val=None):
        if key is None:
            return

        if self._root is None:  # 根节点
            self._root = Node(key, val, 1)
            return
        self._put(self._root, key, val)

    def max(self, node):
        if node.right is None:
            return node
        return self.max(node.right)

    def min(self, node):
        if node.left is None:
            return node
        return self.max(node.left)

    def floor(self, node, key):
        """
        小于等于key的最大key
        """

        if node is None:
            return
        if node.key == key:
            return node
        if key < node.key:
            return self.floor(node.left, key)
        t = self.floor(node.right, key)
        if t is not None:
            return t
        else:
            return node

    def ceiling(self, parameter_list):
        pass


    def select(self, parameter_list):
        pass

    def rank(self, parameter_list):
        pass

    def delete(self, parameter_list):
        pass
    def deleteMin(self, parameter_list):
        pass

    def deleteMax(self, parameter_list):
        pass

    def keys(self, parameter_list):
        pass


if __name__ == "__main__":
    bst = BinarySearchTree()
    bst.put( 1, 'a')
    bst.put( 2, 'b')
    bst.put( 5, 'c')
    bst.put( 4, 'c')
    bst.put( 11, 'c')
    print(bst.get( 6))
    print(bst.max(bst._root))
    print(bst.min(bst._root))
    print(bst.floor(bst._root, 3))
