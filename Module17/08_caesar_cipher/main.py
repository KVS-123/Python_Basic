alphabet = 'абвгдеёжзийклмнопрстуфхцчшщъыьэюяабвгд.,;:"?! '
text = input('Введите сообщение: ')
move = int(input('Введите сдвиг: '))
encrypted_message_list = [alphabet[alphabet.index(i_el)] if alphabet.index(i_el) > 37
                     else alphabet[alphabet.index(i_el) + move]
                     for i_el in text]
encrypted_text = ''
for i in encrypted_message_list:
    encrypted_text += i
print('Зашифрованное сообщение:', encrypted_text)