def generator(a, b):
    return ((a[i], b[i]) for i in range(min(len(a), len(b))))


string = 'abcd'
tpl_num = (10, 20, 30, 40)

print('Строка:', string)
print('Кортеж чисел:', tpl_num)
print()

print('Результат:')
for item in generator(string, tpl_num):
    print(item)