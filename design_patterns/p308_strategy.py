"""策略模式

定义一系列算法， 并将每种算法分别放入独立的类中， 以使算法的对象能够相互替换。

装饰模式可让你更改对象的外表(接口)， 策略则让你能够改变其本质(实现)。

状态模式可被视为策略模式的扩展, 当状态转移方式不明确时就是策略模式。
"""

class Operation:
    def do(self, a: int, b: int):
        pass

class Add(Operation):
    def do(self, a: int, b: int):
        return a + b

class Sub(Operation):
    def do(self, a: int, b: int):
        return a - b

class Context:
    def __init__(self) -> None:
        self.strategy: Operation = Operation()

    def execute_strategy(self, a: int, b: int) -> int:
        return self.strategy.do(a, b)

def main():
    """这里的策略类其实可以直接用高阶函数替换"""

    c = Context()
    c.strategy = Add()
    print(c.execute_strategy(1, 2))
    c.strategy = Sub()
    print(c.execute_strategy(1, 2))

if __name__ == '__main__':
    main()

