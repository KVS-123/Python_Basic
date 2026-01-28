def get_key(dict, val):
    for k, v in dict.items():
        if v == val:
            return k


syn_count = int(input('Введите количество пар слов: '))
syn_dict = dict()

for num in range(1, syn_count+1):
    print(f'{num}-я пара:', end=' ')
    syn_pair = input().lower()
    syn_dict[syn_pair.split(' — ')[0]] = syn_pair.split(' — ')[1]

print()

while True:
    word = input('Введите слово: ').lower()
    if word in syn_dict:
        print('Синоним:', syn_dict[word])
        break
    elif word in syn_dict.values():
        print('Синоним:', get_key(syn_dict, word))
        break
    else:
        print('Такого слова в словаре нет')