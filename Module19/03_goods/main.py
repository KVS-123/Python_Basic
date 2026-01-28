goods = {
    'Лампа': '12345',
    'Стол': '23456',
    'Диван': '34567',
    'Стул': '45678',
}

store = {
    '12345': [
        {'quantity': 27, 'price': 42},
    ],
    '23456': [
        {'quantity': 22, 'price': 510},
        {'quantity': 32, 'price': 520},
    ],
    '34567': [
        {'quantity': 2, 'price': 1200},
        {'quantity': 1, 'price': 1150},
    ],
    '45678': [
        {'quantity': 50, 'price': 100},
        {'quantity': 12, 'price': 95},
        {'quantity': 43, 'price': 97},
    ],
}

for i_el in goods:
    sum_quantity = 0
    sum_price = 0
    for id in range(len(store[goods[i_el]])):
        sum_quantity += store[goods[i_el]][id]['quantity']
        sum_price += store[goods[i_el]][id]['price']
    print(f'{i_el} - {sum_quantity} штук, стоимость {sum_price} рубля')
