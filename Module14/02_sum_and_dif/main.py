def num_sum(num):
    summ = 0
    while num:
        summ += num % 10
        num //= 10
    return summ

def num_count(num):
    count = 0
    while num:
        count += 1
        num //= 10
    return count

N = int(input('Введите число: '))
print('сумма чисел:', num_sum(N))
print('Количество цифр в числе:', num_count(N))
print('Разность суммы и количества цифр:', num_sum(N) - num_count(N))
