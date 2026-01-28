while True:
    password = input('придумайте пароль: ')
    upper_count = 0
    digit_count = 0
    for i_el in password:
        if i_el.isupper():
            upper_count += 1
        elif i_el.isdigit():
            digit_count += 1
    if upper_count >= 1 and digit_count >= 3:
        print('Это надёжный пароль!')
        break
    else:
        print('Пароль ненадёжный. Попробуйте ещё раз.')
