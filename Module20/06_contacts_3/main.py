def add_people():
    key = tuple(input('Введите имя и фамилию нового контакта (через пробел): ').lower().title().split())
    if key in telephone_book:
        print('Такой человек уже есть в контактах.')
        return
    val = int(input('Введите номер телефона: '))
    telephone_book[key] = val
    print('Текущий словарь контактов:', telephone_book)


def search():
    surname = input('Введите фамилию для поиска: ').lower().title()
    for i in telephone_book:
        if i[1] == surname:
            print(i[0], i[1], telephone_book[i])
            return
    print('Такого человека нет в вашей телефонной книге.')


telephone_book = {}
while True:
    print('Введите номер действия:')
    print('1. Добавить контакт')
    print('2. Найти человека')
    answer = int(input('- '))
    if answer == 1:
        add_people()
    elif answer == 2:
        search()