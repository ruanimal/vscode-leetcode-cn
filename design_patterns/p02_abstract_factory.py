"""抽象工厂"""


import os

class Pet:
    def say(self) -> str:
        return '...'

class Cat(Pet):
    pass

class Dog(Pet):
    pass

class ChinaCat(Cat):
    def say(self) -> str:
        return '喵喵喵'

class ChinaDog(Dog):
    def say(self) -> str:
        return '汪汪汪'

class USACat(Cat):
    def say(self) -> str:
        return 'miaow'

class USADog(Dog):
    def say(self) -> str:
        return 'bark'


class PetFactory:
    def create_dog(self) -> Dog:
        pass

    def create_cat(self) -> Cat:
        pass


class ChinaPetFactory:
    def create_dog(self) -> Dog:
        return ChinaDog()

    def create_cat(self) -> Cat:
        return ChinaCat()


class USAPetFactory:
    def create_dog(self) -> Dog:
        return USADog()

    def create_cat(self) -> Cat:
        return USACat()

'''
宠物存在多个维度, 简单工厂难以维护
宠物的种类更有可能扩展, 宠物的国家不太可能扩展.
'''

def main():
    pid = os.getpid()
    if pid % 2 == 0:
        factory = ChinaPetFactory()
    else:
        factory = USAPetFactory()
    cat = factory.create_cat()
    dog = factory.create_dog()
    print(cat.say())
    print(dog.say())


main()
