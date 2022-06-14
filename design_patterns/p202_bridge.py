"""桥接模式, 类似外观模式?

引入桥接类将代码拆分成抽象部分和具体功能实现部分两个层次

如果你想要拆分或重组一个具有多重功能的庞杂类
"""


class Device:
    def __init__(self):
        self._status: int = 0
        self._volume: int = 0

    def is_enabled(self):
        return self._status

    def enable(self):
        self._status = 1

    def disable(self):
        self._status = 0

    def set_volume(self, val: int):
        self._volume = val

    def get_volume(self) -> int:
        return self._volume

class Tv(Device):
    pass

class Radio(Device):
    pass

class RemoteControl:
    def __init__(self, device: Device) -> None:
        self.device = device

    def toggle_power(self):
        return self.device.disable() if self.device.is_enabled() else self.device.enable()

    def volume_up(self):
        return self.device.set_volume(min(self.device.get_volume()+10, 100))

    def volume_down(self):
        return self.device.set_volume(max(self.device.get_volume()-10, 0))

class AdvancedRemoteControl(RemoteControl):
    def mute(self):
        return self.device.set_volume(0)


def main():
    tv = Tv()
    remote = RemoteControl(tv)
    remote.toggle_power()
    print(tv.is_enabled())

    radio = Radio()
    remote = AdvancedRemoteControl(radio)
    remote.volume_up()
    print(radio.get_volume())
    remote.mute()
    print(radio.get_volume())

if __name__ == '__main__':
    main()
