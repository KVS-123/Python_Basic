def is_only_str(val):
    f = '1234567890!@#№$;%:^&?*(){}[]\\/<>.,'
    for i in val:
        if i in f:
            return False
    return True

with open('registrations.txt', 'r', encoding='UTF-8') as info:
    with open('registrations_good.log', 'w', encoding='UTF-8') as good_reg:
        with open('registrations_bad.log', 'w', encoding='UTF-8') as bad_reg:
            for s in info:
                try:
                    name, email, age = s.split()

                    if not is_only_str(name):
                        raise NameError

                    if '@' not in email or '.' not in email:
                        raise SyntaxError

                    if not 10 < int(age) < 99:
                        raise ValueError

                    good_reg.write(s)

                except IndexError:
                    bad_reg.write(s)
                    bad_reg.write('-НЕ присутствуют все три поля\n')

                except NameError:
                    bad_reg.write(s)
                    bad_reg.write('-Поле «Имя» содержит НЕ только буквы\n')

                except SyntaxError:
                    bad_reg.write(s)
                    bad_reg.write('-Поле «Имейл» НЕ содержит @ и . (точку)\n')

                except ValueError:
                    bad_reg.write(s)
                    bad_reg.write('-Поле «Возраст» НЕ является числом от 10 до 99\n')
