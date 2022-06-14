"""组合模式

将对象组合成树状结构, 调用当前元素某个方法具体实现由其子元素提供, 如GUI图形界面绘制

叶节点类代表组合的终端对象。叶节点对象中不能包含任何子对象。叶节点对象
通常会完成实际的工作，组合对象则仅会将工作委派给自己的子部件。
"""

from typing import List

class Graphic:
    def draw(self) -> None:
        pass

class  Dot(Graphic):
    def draw(self) -> None:
        print('.', end='')

class  Line(Graphic):
    def draw(self) -> None:
        print('-', end='')

class CompoundGraphic(Graphic):
    def __init__(self) -> None:
        self.children: List[Graphic] = []

    def add(self, child: Graphic) -> None:
        self.children.append(child)

    def draw(self) -> None:
        print('|', end='')
        for i in self.children:
            i.draw()


def main():
    a = CompoundGraphic()
    b = CompoundGraphic()
    a.add(Dot())
    a.add(Line())
    b.add(Dot())
    a.add(b)
    a.draw()
    print()

if __name__ == '__main__':
    main()

