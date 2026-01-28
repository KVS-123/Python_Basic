ip_adress = input('Введите IP: ').split('.')
for i_el in ip_adress:
    if not i_el.isdigit():
        print(i_el, 'это не целое число.')
        break
    elif int(i_el) > 255:
        print(i_el, 'превышает 255.')
        break
    elif len(ip_adress) != 4:
        print('Адрес — это четыре числа, разделённые точками.')
        break
else:
    print('IP-адрес корректен.')

