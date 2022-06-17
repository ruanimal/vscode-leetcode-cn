"""享元模式(蝇量)

它摒弃了在每个对象中保存所有数据的方式， 通过共享多个对象所共有的相同状态， 让你能在有限的内存容量中载入更多对象。
"""

from typing import List, Dict
from dataclasses import dataclass

@dataclass
class TreeType:
    name: str
    color: str
    texture: str

    def draw(self, x, y):
        print(f'[{id(self)}]{self} at ({x}, {y})')


@dataclass
class Tree:
    type: TreeType
    x: int
    y: int

    def draw(self):
        return self.type.draw(self.x, self.y)

treetypes: Dict[str, TreeType] = {}

@dataclass
class Forest:
    trees: List[Tree]

    def plant(self, x: int, y: int, name: str, color: str, texture: str):
        ttype = treetypes.setdefault(f'{name}-{color}-{texture}', TreeType(name, color, texture))
        self.trees.append(Tree(ttype, x, y))

    def draw(self):
        for i in self.trees:
            i.draw()


def main():
    f = Forest([])
    for i in range(5):
        for j in range(3):
            color = 'red' if i % 2 == 0 else 'black'
            f.plant(i, j, 'tree', color, 'normal')
    f.draw()

if __name__ == '__main__':
    main()

