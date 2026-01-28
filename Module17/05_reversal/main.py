str = input('Введите строку: ')
revers = str[str.index('h') + 1:str.rindex('h')]
print('Развёрнутая последовательность между первым и последним h:', revers)