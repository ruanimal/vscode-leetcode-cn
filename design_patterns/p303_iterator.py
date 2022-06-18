"""迭代器模式

在不暴露集合底层表现形式 （列表、 栈和树等） 的情况下遍历集合中所有的元素。

可以用于简化遍历复杂数据结构 （例如树）, 对遍历方式进行封装
"""

class LoopIterator:
    """环形迭代数组"""

    def __init__(self, vector: list) -> None:
        self.vector: list = vector
        self.pos: int = -1

    def get_next(self):
        if self.has_more():
            self.pos = (self.pos + 1) % len(self.vector)
            return self.vector[self.pos]

    def has_more(self):
        return len(self.vector) > 0

def loop_iterator(vector: list):
    """Python风格迭代器"""

    pos = -1
    while len(vector) > 0:
        pos = (pos+1) % len(vector)
        yield vector[pos]

def main():
    d = [1, 2]
    iter = LoopIterator(d)
    for _ in range(10):
        print(iter.get_next())

    print('--------')
    iter = loop_iterator(d)
    for _ in range(10):
        print(next(iter))

if __name__ == '__main__':
    main()
