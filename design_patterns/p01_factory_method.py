import os

class Pet:
    def say(self) -> str:
        return '...'

class Cat(Pet):
    def say(self) -> str:
        return '喵喵喵'

class Dog(Pet):
    def say(self) -> str:
        return '汪汪汪'


def pet_factory() -> Pet:
    pid = os.getpid()
    if pid % 2 == 0:
        return Dog()
    else:
        return Cat()

def main():
    pet = pet_factory()
    print(pet.say())


main()
