"""外观模式

外观类为包含许多活动部件的复杂子系统提供一个简单的接口。增加抽象层级, 屏蔽底层细节

如果你需要一个指向复杂子系统的直接接口， 且该接口的功能有限， 则可以使用外观模式。
"""

class Warehouse:
    def stock_enough(self):
        return True

class Accountant:
    def do_tax(self):
        pass

class Treasurer:
    def check_pay(self):
        return True

class Delivery:
    def do_deliver(self):
        return 'foobar'

class Shop:
    def handle(self):
        w = Warehouse()
        t = Treasurer()
        d = Delivery()
        a = Accountant()
        if w.stock_enough() and t.check_pay():
            print(d.do_deliver())
            a.do_tax()

def main():
    s = Shop()
    s.handle()

if __name__ == '__main__':
    main()
