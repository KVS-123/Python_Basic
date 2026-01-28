

count = int(input('Введите количество видео карт: '))
card_list = []
max_num = 0

for i in range(count):
    print(i + 1, 'Видеокарта: ', end='')
    num = int(input())
    card_list.append(num)
    if num > max_num:
        max_num = num

print('Старый список видеокарт:', card_list)

for el in card_list:
    if max_num == el:
        card_list.remove(el)

print('Новый список видеокарт:', card_list)


