violator_songs = [
    ['World in My Eyes', 4.86],
    ['Sweetest Perfection', 4.43],
    ['Personal Jesus', 4.56],
    ['Halo', 4.9],
    ['Waiting for the Night', 6.07],
    ['Enjoy the Silence', 4.20],
    ['Policy of Truth', 4.76],
    ['Blue Dress', 4.29],
    ['Clean', 5.83]
]

new_song_list = []
song_count = int(input('Сколько песен выбрать? '))
song_time = 0

for i_num in range(song_count):
    print('Название', str(i_num + 1) + '-й песни:', end=' ')
    song_name = input()
    for i_el in violator_songs:
        if song_name == i_el[0]:
            new_song_list.append(song_name)
            song_time += i_el[1]
    song_time = round(song_time, 2)

print('Общее время звучания песен:', song_time, 'минуты')