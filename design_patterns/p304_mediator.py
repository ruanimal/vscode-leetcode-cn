"""中介模式

能让你减少对象之间混乱无序的依赖关系。 该模式会限制对象之间的直接交互， 迫使它们通过一个中介者对象进行合作。

注意中介对象最后可能演变为过于复杂
"""

from datetime import datetime


class User:
    def __init__(self, name: str, chatroom: 'ChatRoom') -> None:
        self.name = name
        self.chatroom = chatroom

    def send_msg(self, msg):
        self.chatroom.show_msg(self, msg)

class ChatRoom:
    def show_msg(self, user: User, msg: str):
        print(f'{datetime.now()} [{user.name}]: {msg}')


def main():
    """这里的用户可以有多种类型"""

    c = ChatRoom()
    jay = User('jay', c)
    jane = User('jane', c)
    jay.send_msg('hello')
    jane.send_msg('hi')

if __name__ == '__main__':
    main()
