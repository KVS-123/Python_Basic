special_char = '@№$%^&\*()'
path = input('Название файла: ')
for i in special_char:
    if path.startswith(i):
        print('Ошибка: название начинается на один из специальных символов.')
        break
    elif not path.endswith('.txt') and not path.endswith('.docx'):
        print('Ошибка: неверное расширение файла. Ожидалось .txt или .docx.')
        break
else:
    print('Файл назван верно.')