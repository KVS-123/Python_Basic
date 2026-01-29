log_in_list = []


def log_in():
    name = input('Введите имя пользователя: ')
    if name in log_in_list:
        print('Извините, но это имя пользователя уже занято, попробуйте другое')
        log_in()
    else:
        log_in_list.append(name)


def read_chat():
    try:
        with open('chat.txt', 'r', encoding='UTF-8') as chat:
            for s in chat:
                print(s)
    except FileNotFoundError:
        print('Чат не был создан.')


def write_chat(messenge):
    with open('chat.txt', 'a', encoding='UTF-8') as chat:
        name = messenge.split(':')[0]
        if name in log_in_list:
            chat.write(f'{messenge}\n')
        else:
            print('Такого пользователя не существует')


def clear_chat():
    chat = open('chat.txt', 'w', encoding='UTF-8')
    chat.close()


def main():
    print('\nВведите 1, если вы хотите добавить нового пользователя\n'
          'Введите 2, если вы хотите посмотреть чат\n'
          'Нажмите ENTER, если вы хотите написать сообщение')
    answer = input('- ')
    if answer == '1':
        log_in()
    elif answer == '2':
        read_chat()
    elif answer == '':
        print('Введите ваше имя пользователя и сообщение через ":"')
        m = input('- ')
        write_chat(m)
    elif answer == 'clear chat':
        clear_chat()
    else:
        print('Ввод не коректен')

    main()


main()
