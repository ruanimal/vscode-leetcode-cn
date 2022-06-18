"""责任链

责任链会将特定行为转换为被称作处理者的独立对象。
"""

from typing import List

class Component:
    def __init__(self) -> None:
        self.tooltoptext: str = ''
        self.container: 'Container' = None

    def show_help(self):
        if self.tooltoptext:
            print(self.tooltoptext)
        else:
            self.container.show_help()

class Container(Component):
    def __init__(self) -> None:
        super().__init__()
        self.children: List[Component] = []

    def add(self, child: Component):
        self.children.append(child)
        child.container = self


class Button(Component):
    pass

class Panel(Container):
    def __init__(self) -> None:
        super().__init__()
        self.modalHelpText: str = ''

    def show_help(self):
        if self.modalHelpText:
            print(self.modalHelpText)
        else:
            self.container.show_help()


def main():
    panel = Panel()
    panel.modalHelpText = '本面板用于...'
    ok = Button()
    ok.tooltoptext = '确认'
    cancel = Button()
    cancel.tooltoptext = '取消'
    panel.add(ok)
    panel.add(cancel)

    ok.show_help()

if __name__ == '__main__':
    main()
