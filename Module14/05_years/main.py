def years(left_border, right_border):
    for year in range(left_border, right_border + 1):
        for digit in str(year):
            count = 0
            for i in str(year):
                if i == digit:
                    count += 1
            if count == 3:
                print(year)
                break


a = int(input('Введите первый год: '))
b = int(input('Введите второй год: '))
print('Годы от', a, 'до', b, 'с тремя одинаковыми цифрами:')
years(a, b)
