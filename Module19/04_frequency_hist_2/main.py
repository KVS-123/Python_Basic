text = input('Введите текст: ')
text_dict = dict()

for i_el in text:
    text_dict[i_el] = text.count(i_el)

inverted_dict = dict()
key_set = set(text_dict.values())

for _ in range(len(key_set)):
    set_values = set()
    for i in text:
        if text.count(i) == min(key_set):
            set_values.add(i)
    inverted_dict[min(key_set)] = set_values
    key_set.remove(min(key_set))

for key in inverted_dict:
    print(key, ':', inverted_dict[key])
