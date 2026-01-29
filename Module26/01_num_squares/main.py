class Iterator:
    def __init__(self, num):
        self.count = 0
        self.num = num

    def __iter__(self):
        self.count = 0
        return self

    def __next__(self):
        if self.count != self.num:
            self.count += 1
            return self.count ** 2
        else:
            raise StopIteration


def gen(num):
    count = 0
    while count != num:
        count += 1
        yield count ** 2


n = int(input('Введите число '))

print('Первый способ: ')
first = Iterator(n)
for f in first:
    print(f, end=' ')

print('\nВторой способ: ')
second = gen(n)
for s in second:
    print(s, end=' ')

print('\nТретий способ: ')
third = (t ** 2 for t in range(1, n+1))
for t in third:
    print(t, end=' ')
