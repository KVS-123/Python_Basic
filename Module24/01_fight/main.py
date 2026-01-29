import random


class Unit:
    health = 100
    damage = 20

    def __init__(self, name):
        self.name = name
        self.alive = True

    def is_alive(self):
        if self.alive:
            return True
        else:
            print(self.name, 'погиб!')
            return False

    def take_damage(self, damage):
        self.health -= damage
        if self.health <= 0:
            self.alive = False
            return False
        print(self.health)
        return self.health

    def hit(self, enemy):
        print(self.name, 'атакует!')
        return enemy.take_damage(self.damage)


def fight(player1, player2):
    while True:
        if not player1.is_alive():
            print(player2.name, 'победил!')
            break

        if not player2.is_alive():
            print(player1.name, 'победил!')
            break

        if random.randint(1, 6) % 2 == 0:
            player1.hit(second)
        else:
            player2.hit(first)


first = Unit('first')
second = Unit('second')

fight(first, second)


