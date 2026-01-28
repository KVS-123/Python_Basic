def cycle(n):
    if n == 1:
        print(n)
        return 1
    cycle(n - 1)
    print(n)


num = int(input('Введите num: '))
cycle(num)