import random


class House:
    meal = 50
    money = 0


class Human:
    live = True
    days_lived = 0

    def __init__(self, name, satiety, house):
        self.name = name
        self.satiety = satiety
        self.house = house

    def eat(self):
        self.satiety += 10
        self.house.meal -= 10

    def work(self):
        self.satiety -= 10
        self.house.money += 10

    def play(self):
        self.satiety -= 10

    def shopping(self):
        self.house.meal += 10
        self.house.money -= 10

    def live_day(self):
        if self.live:
            self.days_lived += 1

    def death(self):
        if self.satiety <= 0:
            self.live = False
            print(f'{self.name} мертв')


house_1 = House()
first = Human('Иван', 40, house_1)
second = Human('Наталья', 10, house_1)
while (first.live and second.live) and first.days_lived != 365:
    print('День', first.days_lived + 1)
    for human in [first, second]:
        cube = random.randint(1, 6)
        if human.satiety < 20:
            human.eat()
            print(f'{human.name} поел')
        elif human.house.meal < 10:
            human.shopping()
            print(f'{human.name} пошёл в магазин')
        elif human.house.money < 50:
            human.work()
            print(f'{human.name} пошёл на работу')
        elif cube == 1:
            human.work()
            print(f'{human.name} пошёл на работу')
        elif cube == 2:
            human.eat()
            print(f'{human.name} поел')
        else:
            human.play()
            print(f'{human.name} играет')
        human.death()
        human.live_day()
    print()
