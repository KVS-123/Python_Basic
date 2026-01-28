guests = ['Петя', 'Ваня', 'Саша', 'Лиза', 'Катя']

while True:
    print('Сейчас на вечеринке', len(guests), 'человек:', guests)
    come_or_gone = input('Гость пришёл или ушёл? ')
    if come_or_gone == 'Пора спать':
        print('Вечеринка закончилась, все легли спать')
        break
    guest_name = input('Имя гостя: ')
    if come_or_gone == 'пришёл' and len(guests) < 6:
        print('Привет,', guest_name + '!')
        guests.append(guest_name)
    elif come_or_gone == 'пришёл' and len(guests) >= 6:
        print('Прости, ' + guest_name + ', но мест нет.')
    elif come_or_gone == 'ушёл':
        print('Пока,', guest_name + '!')
        guests.remove(guest_name)
    print()
