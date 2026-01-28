def isPolydrome(list):
    for i in range(len(list) // 2):
        if list[i] != list[-1 - i]:
            return False
    return True

num_list = []
needed_num = []
num_count = int(input('Кол-во чисел: '))
for _ in range(num_count):
    number = int(input('Число: '))
    num_list.append(number)

print('Последовательность:', num_list)
if isPolydrome(num_list) == False:
    for _ in range(len(num_list)):
        needed_num.append(num_list[0])
        num_list.remove(num_list[0])
        if isPolydrome(num_list):
            break
    print('Нужно приписать чисел:', len(needed_num))
    print('Сами числа:', needed_num)
else:
    print('эта последовательность уже семитрична')

