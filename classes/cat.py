from random import randint


class Cat:
    def __init__(self, name):
        self.name = name
        self.mood = 100
        self.fullness = 50
        self.home = None

    def __str__(self):
        return f"Я -{self.name},настроение -{self.mood},сытсость -{self.fullness}"

    def eat(self):
        if self.home is None:
            print(f'У {self.name}a нет дома')
        else:
            self.home.cat_bowl -= 10
            self.fullness += 10
            print(f'{self.name} поел')

    def settle_in_the_house(self, house):
        self.home = house
        print(f'{self.name} вселился в доm')

    def sleep(self):
        self.fullness -= 20
        print(f'{self.name} спал всеь день')

    def act(self):
        if self.fullness <= 0:
            print(f'{self.name} Rip...')
            return
        dice = randint(1, 6)
        if dice == 1:
            self.eat()
        else:
            self.sleep()


class House:
    def __init__(self):
        self.cat_bowl = 100
        if self.cat_bowl < 10:
            return self.cat_bowl * 2  # кормим кота


murzik = Cat(name='Мурзик')

print(murzik)
murzik.eat()
my_home = House()
murzik.settle_in_the_house(house=my_home)

for day in range(1, 31):
    print(f'******************* день {day}')
    murzik.act()

    if murzik.fullness <= 0:
        print(f'{murzik.name} мертв!')
        break
    print(murzik)
