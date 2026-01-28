violator_songs = {
    'World in My Eyes': 4.86,
    'Sweetest Perfection': 4.43,
    'Personal Jesus': 4.56,
    'Halo': 4.9,
    'Waiting for the Night': 6.07,
    'Enjoy the Silence': 4.20,
    'Policy of Truth': 4.76,
    'Blue Dress': 4.29,
    'Clean': 5.83
}

count_song = int(input('Сколько песен выбрать? '))
count = 0
sum_minutes = 0

while count != count_song:
    name = input('Введите название песни: ')
    if name in violator_songs:
        sum_minutes += violator_songs[name]
        count += 1
    else:
        print('Такой песни нет!')

sum_minutes = round(sum_minutes, 2)
print(f'\nОбщее время звучания песен: {sum_minutes} минуты')