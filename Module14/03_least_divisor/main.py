def minDivisor(num):
    div = 2
    while num % div != 0:
        div += 1
    return div

number = int(input('Введите число: '))
print('Наименьший делитель, отличный от единицы:', minDivisor(number))
