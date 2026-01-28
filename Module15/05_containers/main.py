count = int(input('Количество контейнеров: '))
containers_list = []

for _ in range(count):
    container = int(input('Введите вес контейнера: '))
    if container <= 200:
        containers_list.append(container)
    else:
        print('Контейнер слишком тяжёлый!')

new_container = int(input('Введите вес нового контейнера: '))
number = 0

if new_container <= 200:
    for el in containers_list:
        number += 1
        if new_container > el:
            break
    print('Номер, который получит новый контейнер:', number)
else:
    print('Контейнер слишком тяжёлый!')
