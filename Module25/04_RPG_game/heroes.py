import random
from monsters import MonsterBerserk, MonsterHunter


class Hero:

    max_hp = 150
    start_power = 10

    def __init__(self, name):
        self.name = name
        self.__hp = self.max_hp
        self.__power = self.start_power
        self.__is_alive = True

    def get_hp(self):
        return self.__hp

    def set_hp(self, new_value):
        self.__hp = max(new_value, 0)

    def get_power(self):
        return self.__power

    def set_power(self, new_power):
        self.__power = new_power

    def is_alive(self):
        return self.__is_alive

    def attack(self, target):
        raise NotImplementedError("Вы забыли переопределить метод Attack!")

    def take_damage(self, damage):
        print("\t", self.name, "Получил удар с силой равной = ", round(damage), ". Осталось здоровья - ", round(self.get_hp()))
        if self.get_hp() <= 0:
            self.__is_alive = False

    def make_a_move(self, friends, enemies):
        self.set_power(self.get_power() + 0.1)

    def __str__(self):
        raise NotImplementedError("Вы забыли переопределить метод __str__!")


class Healer(Hero):

    def __init__(self, name):
        super().__init__(name)
        self.__power = self.start_power * 3

    def __str__(self):
        return 'Name: {0} | HP: {1}'.format(self.name, self.get_hp())

    def attack(self, target):
        target.take_damage(self.get_power() * 0.5)

    def take_damage(self, damage):
        self.set_hp(self.get_hp() - 1.2 * damage)
        super().take_damage(damage)

    def healing(self, target):
        target.set_hp(target.get_hp() + self.get_power())
        print("\t", target.name, "был исцелен на", round(self.get_power()), ". Осталось здоровья - ",
              round(target.get_hp()))

    def make_a_move(self, friends, enemies):
        print(self.name, end='')
        min_hp = 500
        friend_id = 0
        enemies_min_hp = 500
        enemy = 0
        for friend in friends:
            if friend.get_hp() < min_hp:
                min_hp = friend.get_hp()
                friend_id = friend
        if friend_id.get_hp() < 100:
            self.healing(friend_id)
        else:
            for mob in enemies:
                if mob.get_hp() < enemies_min_hp:
                    enemies_min_hp = mob.get_hp()
                    enemy = mob
            if enemy != 0:
                self.attack(enemy)
        super().make_a_move(friends, enemies)


class Tank(Hero):

    def __init__(self, name):
        super().__init__(name)
        self.defense = 1
        self.is_raised = False

    def __str__(self):
        return 'Name: {0} | HP: {1}'.format(self.name, self.get_hp())

    def attack(self, target):
        target.take_damage(self.get_power() * 0.5)

    def take_damage(self, damage):
        self.set_hp(self.get_hp() - (damage/self.defense))
        super().take_damage(damage)

    def raise_shield(self):
        if not self.is_raised:
            self.is_raised = True
            self.defense *= 2
            self.set_power(self.get_power() * 0.5)

    def lower_shield(self):
        if self.raise_shield():
            self.is_raised = False
            self.defense *= 0.5
            self.set_power(self.get_power() * 2)

    def make_a_move(self, friends, enemies):
        print(self.name, end='')
        enemies_min_hp = 500
        enemy = 0
        if self.get_hp() < 160:
            if not self.is_raised:
                self.raise_shield()
            else:
                for mob in enemies:
                    if isinstance(mob, MonsterHunter):
                        self.attack(mob)
                        break
                else:
                    for mob in enemies:
                        if mob.get_hp() < enemies_min_hp:
                            enemies_min_hp = mob.get_hp()
                            enemy = mob
                    if enemy != 0:
                        self.attack(enemy)
        else:
            if self.is_raised:
                self.lower_shield()
            else:
                for mob in enemies:
                    if isinstance(mob, MonsterHunter):
                        self.attack(mob)
                        break
                else:
                    for mob in enemies:
                        if mob.get_hp() < enemies_min_hp:
                            enemies_min_hp = mob.get_hp()
                            enemy = mob
                    if enemy != 0:
                        self.attack(enemy)
        super().make_a_move(friends, enemies)


class Attacker(Hero):
    def __init__(self, name):
        super().__init__(name)
        self.power_multiply = 4

    def __str__(self):
        return 'Name: {0} | HP: {1}'.format(self.name, self.get_hp())

    def attack(self, target):
        target.take_damage(self.get_power() * self.power_multiply)
        self.power_down()

    def take_damage(self, damage):
        self.set_hp(self.get_hp() - damage * (self.power_multiply * 0.5))
        super().take_damage(damage)

    def power_up(self):
        self.power_multiply *= 2

    def power_down(self):
        self.power_multiply *= 0.5

    def make_a_move(self, friends, enemies):
        print(self.name, end='')
        enemies_min_hp = 500
        enemy = 0
        if self.power_multiply < 4:
            self.power_up()
        else:
            for mob in enemies:
                if isinstance(mob, MonsterBerserk):
                    self.attack(mob)
                    break
            else:
                for mob in enemies:
                    if mob.get_hp() < enemies_min_hp:
                        enemies_min_hp = mob.get_hp()
                        enemy = mob
                self.attack(enemy)
        super().make_a_move(friends, enemies)
