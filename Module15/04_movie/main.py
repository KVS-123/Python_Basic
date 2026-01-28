films = ['Крепкий орешек', 'Назад в будущее', 'Таксист',
         'Леон', 'Богемская рапсодия', 'Город грехов',
         'Мементо', 'Отступники', 'Деревня']

count = int(input('Сколько фильмов вы хотите добавить? '))
favoriteFilmList = []

for _ in range(count):
    film = input('Введите название фильма: ')
    for el in films:
        if el == film:
            favoriteFilmList.append(film)
            break
    else:
        print('Ошибка: фильма', film, 'у нас нет :(')

print('Ваш список любимых фильмов:', favoriteFilmList)