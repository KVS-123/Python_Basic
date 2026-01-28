shop = [['каретка', 1200], ['шатун', 1000], ['седло', 300],
        ['педаль', 100], ['седло', 1500], ['рама', 12000],
        ['обод', 2000], ['шатун', 200], ['седло', 2700]]

detail_name = input('Название детали: ')
detail_count = 0
price = 0
for i_el in shop:
        detail_count += i_el.count(detail_name)
        if i_el[0] == detail_name:
               price += i_el[1]
print('Кол-во деталей —', detail_count)
print('Общая стоимость —', price)