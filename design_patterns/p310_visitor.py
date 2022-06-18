"""访问者模式

能将算法与其所作用的对象隔离开来。
"""

from dataclasses import dataclass

@dataclass
class Shape:
    def draw(self):
        print(repr(self))

@dataclass
class Dot(Shape):
    x: int
    y: int

@dataclass
class Circle(Shape):
    x: int
    y: int
    radius: int


class ExportVisitor:
    def visit(self, s: Shape):
        if isinstance(s, Dot):
            return (s.x, s.y)
        elif isinstance(s, Circle):
            return (s.x, s.y, s.radius)
        raise TypeError(s)

def main():
    shapes = [Dot(1, 2), Dot(3, 4), Circle(3, 3, 1)]
    for i in shapes:
        i.draw()
    ev = ExportVisitor()
    print([ev.visit(i) for i in shapes])

if __name__ == '__main__':
    main()
