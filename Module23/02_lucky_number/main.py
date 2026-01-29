import random

summ = 0
try:
    with open('out_file.txt', 'w') as numbers:
        while summ < 777:
            if random.randint(0, 13) == 7:
                raise BaseException
            num = int(input('Введите число: '))
            summ += num
            numbers.write(f'{str(num)}\n')
        else:
            print('Вы успешно выполнили условие для выхода из порочного цикла!')

except BaseException:
    print('Вас постигла неудача!')
