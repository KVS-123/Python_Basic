str = input('Введите строку: ')
str_dict = dict()
count = 0

for key in str:
    str_dict[key] = str.count(key)

for i_elem in str_dict:
    if str_dict[i_elem] % 2 != 0:
        count += 1
        if count > 1:
            print('Нельзя сделать палиндромом')
            break
else:
    print("Можно сделать палиндромом")