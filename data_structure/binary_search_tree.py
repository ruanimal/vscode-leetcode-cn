
class BinarySearchTree:
    class Node(object):
        def __init__(self, key, val, n):
            self.key = key
            self.val = val
            self.left = None
            self.right = None
            self.n = n  # 节点总数

    def __init__(self):
        self._root = None

    def size(self, node=None):
        if node is None:
            node = self._root
        return node.n

    def get(self, node=-1, key=None):
        if node == -1:
            node = self._root
        if node is None:
            return
        if key is None:
            return
        if key < node.key:
            return self.get(node.left, key)
        elif key > node.key:
            return self.get(node.right, key)
        else:
            return node.val

    def put(self, node=-1, key, val):
        if node == -1:  # 根节点
            self._root = Node(key, val)

        if node is None:   # 叶节点
            return Node(key, val)
        if key < node.key:
            node.left = self.put(node.left, key, val)
        elif key > node.key:
            node.right = self.put(node.right, key, val)
        else:
            node.val = val
        node.n = self.size(node.left) + self.size(node.right) + 1
        return node

    def max(self, parameter_list):
        pass

    def min(self, parameter_list):
        pass

    def floor(self, parameter_list):
        pass

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
