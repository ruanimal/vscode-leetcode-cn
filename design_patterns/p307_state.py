"""状态模式

让你能在一个对象的内部状态变化时改变其行为， 使其看上去就像改变了自身所属的类一样。

如果状态机只有很少的几个状态， 或者很少发生改变， 那么应用该模式可能会显得小题大作。
"""

class State:
    def do_start(self):
        pass

    def do_stop(self):
        pass

class StartState(State):
    def do_start(self, context: 'AudioPlayer'):
        print('Player is already started, skip.')

    def do_stop(self, context: 'AudioPlayer'):
        print('Player is stopping')
        context.state = StopState()

class StopState(State):
    def do_start(self, context: 'AudioPlayer'):
        print('Player is in starting')
        context.state = StartState()

    def do_stop(self, context: 'AudioPlayer'):
        print('Player is already stopped, skip.')

class AudioPlayer:
    def __init__(self) -> None:
        self.state: State = StopState()

    def stop(self):
        self.state.do_stop(self)

    def start(self):
        self.state.do_start(self)

def main():
    c = AudioPlayer()
    c.start()
    c.start()
    c.stop()
    c.stop()

if __name__ == '__main__':
    main()
