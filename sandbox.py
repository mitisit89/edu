import math


nums = 12.2
math.ceil(nums)


class Animal:
    def __init__(self, name):
        self.speed = 0
        self.name = name

    def run(self, speed):
        self.speed = speed
        print(f'{self.name},бежит с скоростю {self.speed}')

    @staticmethod
    def stop():
        speed = 0
        print(f'{speed} are stop')


class Rabbit(Animal):
    def hide(self):
        print('Rabbit are hiding!')


rabbit = Rabbit('Black Rabbit')
rabbit.run(2)
rabbit.hide()
Rabbit.stop()


def m(a=None):
    return a


m(1)
