n = int(input('Введите число: '))
n_list = []
for i in range(1, n + 1, 2):
    n_list.append(i)
print('Список из нечётных чисел от одного до N:', n_list)