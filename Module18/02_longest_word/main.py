text = input('Введите текст: ')
lenn = 0
longest_line = ''
for i_str in text.split():
    if len(i_str) > lenn:
        lenn = len(i_str)
        longest_line = i_str
print('Самое длинное слово:', longest_line)
print('Длина этого слова:', lenn)

