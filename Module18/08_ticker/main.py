first_str = input('Первая строка: ')
second_str = input('Вторая строка: ')
count = 0
while first_str != second_str:
    count += 1
    first_str = first_str[-1] + first_str[:-1]

    if count > len(first_str):
        print('Вторую строку нельзя получить из первой с помощью циклического сдвига.')
        break
else:
    print('Вторая строка получается из первой со сдвигом', count)