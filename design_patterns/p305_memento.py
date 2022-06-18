"""备忘录模式

不暴露对象实现细节的情况下保存和恢复对象之前的状态。

本质是让数据所有者来决定如何保存和重载数据, 数据储存则并不关心数据具体内容.
"""

from typing import List
from datetime import datetime

class LocationMemento:
    def __init__(self, state: str) -> None:
        self.state = state

class CareTaker:
    def __init__(self) -> None:
        self.mementos: List = []

    def add(self, memento: LocationMemento):
        self.mementos.append(memento)

    def get(self, index: int) -> LocationMemento:
        return self.mementos[index]

class Traveller:
    def __init__(self, name: str, age: int) -> None:
        self.name = name
        self.age = age
        self.location: str = 'home'

    def save_location(self) -> LocationMemento:
        return LocationMemento(self.location)

    def load_location(self, memento: LocationMemento):
        self.goto(memento.state)

    def goto(self, location: str):
        self.location = location
        print(f'{datetime.now()} [{self.name}]: arrive {location}')

def main():
    ct = CareTaker()
    me = Traveller('Jay', 18)
    me.goto('Beijing')
    ct.add(me.save_location())
    me.goto('Shanghai')
    ct.add(me.save_location())
    me.load_location(ct.get(0))

if __name__ == '__main__':
    main()
