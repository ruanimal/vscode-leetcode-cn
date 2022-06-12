"""适配器模式

当你想把接口不兼容的代码用起来的时候

实现上也可以用__getattribute__进行方法的自动转发
"""

from io import StringIO

class USBDisk:
    def __init__(self):
        self.storage = StringIO()

    def write(self, data: str):
        self.storage.write(data)

    def read(self) -> str:
        return self.storage.getvalue()

class MicroUSBDisk(USBDisk):
    pass

class TypeCUSBDisk(USBDisk):
    pass

class MicroToTypecAdapter(TypeCUSBDisk):
    def __init__(self, device: MicroUSBDisk):
        self.device = device

    def write(self, data: str):
        self.device.write(data)

    def read(self) -> str:
        return self.device.read()


class MacBook2018:
    def __init__(self):
        self._usbbus = None

    def connect(self, usb: TypeCUSBDisk):
        assert isinstance(usb, TypeCUSBDisk), 'macbook only support typec'
        self._usbbus = usb

    def send(self, data: str):
        self._usbbus.write(data)

    def recv(self) -> str:
        return self._usbbus.read()


def main():
    disk = MicroUSBDisk()
    disk.write('1234')
    mac = MacBook2018()
    try:
        mac.connect(disk)
    except AssertionError as e:
        print(e)
    adapter = MicroToTypecAdapter(disk)
    mac.connect(adapter)
    print(mac.recv())

if __name__ == '__main__':
    main()
