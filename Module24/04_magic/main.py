
class Water:
    def __add__(self, elem):
        if isinstance(elem, Air):
            return Storm
        elif isinstance(elem, Fire):
            return Steam
        elif isinstance(elem, Earth):
            return Mud
        else:
            print('Эти элементы не складываются')


class Air:
    def __add__(self, elem):
        if isinstance(elem, Water):
            return Storm
        elif isinstance(elem, Fire):
            return Lightning
        elif isinstance(elem, Earth):
            return Dust
        else:
            print('Эти элементы не складываются')


class Fire:
    def __add__(self, elem):
        if isinstance(elem, Water):
            return Steam
        elif isinstance(elem, Air):
            return Lightning
        elif isinstance(elem, Earth):
            return Lava
        else:
            print('Эти элементы не складываются')


class Earth:
    def __add__(self, elem):
        if isinstance(elem, Water):
            return Mud
        elif isinstance(elem, Air):
            return Dust
        elif isinstance(elem, Fire):
            return Lava
        else:
            print('Эти элементы не складываются')


class Storm:
    elem = 'Шторм'


class Steam:
    elem = 'Пар'


class Mud:
    elem = 'Грязь'


class Lightning:
    elem = 'Молния'


class Dust:
    elem = 'Пыль'


class Lava:
    elem = 'Лава'


a = Air()
b = Water()
c = a + b
print(c.elem)

