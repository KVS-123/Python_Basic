import copy

site = {
    'html': {
        'head': {
            'title': 'Куплю/продам телефон недорого'
        },
        'body': {
            'h2': 'У нас самая низкая цена на iphone',
            'div': 'Купить',
            'p': 'продать'
        }
    }
}


def copy_site(site_f):
    question = int(input('Сколько сайтов: '))
    for _ in range(question):
        name = input('Введите название продукта для нового сайта: ')
        print(f'Сайт для {name}:')
        site_copy = copy.deepcopy(site_f)
        site_copy['html']['head']['title'] = f'Куплю/продам {name} недорого'
        site_copy['html']['body']['h2'] = f'У нас самая низкая цена на {name}'
        print('site')
        print_site(site_copy)


def print_site(site_copy, space=1):
    for i in site_copy:
        print('\t' * space, i)
        if isinstance(site_copy[i], dict):
            print_site(site_copy[i], space + 1)
        else:
            print('\t' * (space + 1), ''.join(site_copy[i]))


copy_site(site)
