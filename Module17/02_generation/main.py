num = int(input('Введите длину списка: '))
result = [(1 if x % 2 == 0 else x % 5) for x in range(num)]
print('Результат:', result)