
char_count = 0
string = 0
try:
    with open('people.txt', 'r', encoding='UTF-8') as people:
        for s in people:
            try:
                string += 1
                length = len(s)
                if s.endswith('\n'):
                    length -= 1
                if length < 3:
                    raise BaseException

            except BaseException:
                print(f'Ошибка: менее трёх символов в строке {string}.')

            finally:
                char_count += length
finally:
    print('Общее количество символов:', char_count)
