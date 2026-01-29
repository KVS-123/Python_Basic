import re

phone = ['9999999999', '999999-999', '99999x9999']
pattern = re.compile(r'[89]\d{1,9}')

for num in phone:
    print(f'{phone.index(num) + 1} номер:', end=' ')
    if num in pattern.findall(num):
        print('всё в порядке')
    else:
        print('не подходит')