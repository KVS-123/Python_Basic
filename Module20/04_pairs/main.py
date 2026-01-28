import random

origin_list = [random.randint(1, 10) for _ in range(10)]
new_list = [(origin_list[i], origin_list[i+1]) for i in range(0, len(origin_list), 2)]

print('Оригинальный список:', origin_list)
print('Новый список:', new_list)