"""单例模式
用于保证一个类全局只有一个对象, 一般用在类的实例创建成本较高的场景

在python简单使用场景中, 常常可以使用模块或者类对象等全局对象替代
"""

class _SingletonMeta(type):
    _instances = {}
    def __call__(cls, *args, **kwargs):
        if cls not in cls._instances:
            cls._instances[cls] = super(_SingletonMeta, cls).__call__(*args, **kwargs)
        return cls._instances[cls]

class Singleton(metaclass=_SingletonMeta):
    pass

class God(Singleton):
    pass

def main():
    god = God()
    new_god = God()
    assert god is new_god

if __name__ == '__main__':
    main()

