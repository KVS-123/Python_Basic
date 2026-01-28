word = list(input('Введите слово: '))
x = 0
for index in range(len(word) // 2):
    x -= 1
    if word[index] != word[x]:
        print('Слово не является палиндромом')
        break
else:
    print('Слово является палиндромом')