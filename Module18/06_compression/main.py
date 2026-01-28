string = input('Введите строку: ') + ' '
new_string = ''
str_list = [i for i in string]
char = str_list[0]
count = 0
for i_el in str_list:
    if char == i_el:
        count += 1
    else:
        new_string += char + str(count)
        char = i_el
        count = 1
print('Закодированная строка:', new_string)