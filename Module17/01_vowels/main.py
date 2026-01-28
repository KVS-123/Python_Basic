vowel_str = 'ауоыиэяюеё'
text = input('Введите текст: ')
vowel_list = [i_el for i_el in text if i_el in vowel_str]
print(vowel_list)
