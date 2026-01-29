import random


class Child:
    c_state = {0: 'спокоен', 1: 'активен', 2: 'гиперактивен', 3: 'бесится'}
    h_state = {0: 'сытый', 1: 'хочет перекусить', 2: 'голоден'}

    def __init__(self, name, age):
        self.name = name
        self.age = age
        self.calm_state = random.randint(0, 3)
        self.hunger_state = random.randint(0, 2)

    def calm(self, coef):
        if self.calm_state > 0:
            self.calm_state -= coef
        print(f'{self.name} {self.c_state[self.calm_state]}')

    def feed(self):
        if self.hunger_state > 0:
            self.hunger_state -= 1
        print(f'{self.name} {self.h_state[self.hunger_state]}')


class Parent:
    def __init__(self, name, age, children):
        self.name = name
        self.age = age
        self.children = list()
        for i in children:
            if age - i[1] > 15:
                self.children.append(Child(i[0], i[1]))
            else:
                print('Разница в возрасте родителя и ребёнка слишком маленькая!')

    def get_info(self):
        print(f'{self.name} {self.age} дети:')
        for child in self.children:
            print(child.name)

    def calm(self, name):
        for child in self.children:
            if name == child.name:
                print('\nвыберите, как вы хотите успокоить ребенка:')
                print('1-попросить успокоиться, 2-накричать')
                answer = int(input('-'))
                child.calm(answer)

    def feed(self, name):
        for child in self.children:
            if name == child.name:
                child.feed()


parent_name = input('Введите имя родителя: ')
parent_age = int(input('Введите возраст родителя: '))
children_count = int(input('Количество детей - '))
children_list = list()

for _ in range(children_count):
    print()
    child_name = input('Введите имя ребёнка: ')
    child_age = int(input('Введите возраст ребёнка: '))
    children_list.append([child_name, child_age])


first = Parent(parent_name, parent_age, children_list)
first.get_info()
first.calm('Витя')
first.feed('Витя')

