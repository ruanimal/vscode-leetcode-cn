"""观察者模式

允许你定义一种订阅机制， 可在对象事件发生时通知多个 “观察” 该对象的其他对象。

独立于其他代码的核心功能将作为发布者； 其他代码则将转化为一组订阅类。
"""

from typing import List, Dict

class WishBoard:
    def __init__(self) -> None:
        self.subscribers: Dict[str, List['Customer']] = {}

    def subscribe(self, customer: 'Customer', game: str):
        self.subscribers.setdefault(game, []).append(customer)

    def unsubscribe(self, customer: 'Customer', game: str):
        self.subscribers.setdefault(game, []).remove(customer)

    def notify(self, game: str):
        for i in self.subscribers.get(game, []):
            i.buy(game)

class GameShop:
    def __init__(self, wishboard: WishBoard) -> None:
        self.games: Dict[str, int] = {}
        self.wishboard = wishboard

    def restock(self, game: str, count: int):
        self.games[game] = self.games.get(game, 0) + count
        self.wishboard.notify(game)

class Customer:
    def __init__(self, name: str) -> None:
        self.name = name

    def buy(self, game: str):
        print(f'{self.name} buy {game!r}')


def main():
    jay = Customer('jay')
    tom = Customer('tom')
    board = WishBoard()
    board.subscribe(jay, 'Fallout 4')
    board.subscribe(jay, 'Mirror 2')
    board.subscribe(tom, 'PUBG')
    shop = GameShop(board)
    shop.restock('PUBG', 1)
    shop.restock('Mirror 2', 1)

if __name__ == '__main__':
    main()
