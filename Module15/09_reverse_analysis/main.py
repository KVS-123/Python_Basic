numbers_list = [7, 14, 3, 18, 21, 10, 9, 6]

for el in numbers_list:
    if el % 2 != 0:
        numbers_list.remove(el)

print('Отсортированный список: ', end='')

for index in range(-1, -len(numbers_list) - 1, -1):
    print(numbers_list[index], end=' ')


# Список чисел для работы (итоговый алгоритм проверьте на разных списках, придуманных самостоятельно):
# numbers_list = [7, 14, 3, 18, 21, 10, 9, 6]
