import math
def distance_to_point(x, y):
    dist = math.sqrt(x ** 2 + y ** 2)
    return dist

print('Введите координаты монетки:')
x = float(input('X: '))
y = float(input('Y: '))
r = int(input('Введите радиус: '))
if distance_to_point(x, y) > r:
    print('Монетки в области нет')
else:
    print('Монетка где-то рядом')
