main_list = [1, 5, 3]
first_side_list = [1, 5, 1, 5]
second_side_list = [1, 3, 1, 5, 3, 3]

main_list.extend(first_side_list)
count_5 = main_list.count(5)
for _ in range(count_5):
    main_list.remove(5)

main_list.extend(second_side_list)
count_3 = main_list.count(3)

print('Кол-во цифр 5 при первом объединении:', count_5)
print('Кол-во цифр 3 при первом объединении:', count_3)
print('Итоговый список:', main_list)

