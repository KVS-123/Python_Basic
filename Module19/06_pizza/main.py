order_count = int(input('Введите количество заказов: '))
data_dict = dict()

for num in range(1, order_count+1):
    print(f'{num}-й заказ:', end=' ')
    order = input().split()
    if order[0] in data_dict:
        if order[1] in data_dict[order[0]]:
            data_dict[order[0]][order[1]] += int(order[2])
        else:
            data_dict[order[0]][order[1]] = order[2]
    else:
        data_dict[order[0]] = dict({order[1]: int(order[2])})

for elem_1 in sorted(data_dict):
    print(f'\n{elem_1}:')
    for elem_2 in sorted(data_dict[elem_1]):
        print(f'\t{elem_2}: {data_dict[elem_1][elem_2]}')
