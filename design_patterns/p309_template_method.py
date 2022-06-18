"""模板方法

在超类中定义了一个算法的框架， 允许子类在不修改结构的情况下重写算法的特定步骤。

通过子类抑制默认步骤实现可能会导致违反里氏替换原则。

工厂方法模式是模板方法模式的一种特殊形式。

模板方法基于继承机制, 策略模式基于组合机制.
模板方法在类层次上运作, 因此它是静态的。
策略在对象层次上运作， 因此允许在运行时切换行为。
"""


class SoupMaker:
    def make(self):
        self.add_water()
        self.add_material()
        self.heat()
        self.add_flavouring()
        print('done')

    def add_water(self):
        print('add 500ml water')

    def add_material(self):
        print('add dummy')

    def add_flavouring(self):
        print('add 1g salt')

    def heat(self):
        print('heating 5 min')


class EggSoupMaker(SoupMaker):
    def add_material(self):
        print('add one egg')

class MeatSoupMaker(SoupMaker):
    def add_material(self):
        print('add 100g pork')


def main():
    a = EggSoupMaker()
    a.make()
    b = MeatSoupMaker()
    b.make()

if __name__ == '__main__':
    main()
