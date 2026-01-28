people_count = int(input('Кол-во человек: '))
people_list = list(range(1, people_count + 1))
reader_num = int(input('Какое число в считалке? '))
print('Значит, выбывает каждый', str(reader_num) + '-й человек', end='\n\n')

index = -1
while len(people_list) > 1:
    print('Текущий круг людей:', people_list)
    if people_list[index] == people_list[-1]:
        print('Начало счёта с номера', people_list[0])
    else:
        print('Начало счёта с номера', people_list[index + 1])

    for _ in range(reader_num):
        if people_list[index] == people_list[-1]:
            index = 0
        else:
            index += 1
    else:
        print('Выбывает человек под номером', people_list[index], end='\n\n')
        people_list.remove(people_list[index])
        index -= 1
else:
    print('Остался человек под номером', people_list[index])