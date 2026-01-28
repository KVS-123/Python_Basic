def find_key(dct, key, depth=5):
	if depth >= 1:
		if key in dct:
			return dct[key]
	else:
		return None
	for i in dct.values():
		if isinstance(i, dict):
			result = find_key(i, key, depth-1)
			if result:
				break
	else:
		result = None
	return result


site = {
	'html': {
		'head': {
			'title': 'Мой сайт'
		},
		'body': {
			'h2': 'Здесь будет мой заголовок',
			'div': 'Тут, наверное, какой-то блок',
			'p': 'А вот здесь новый абзац'
		}
	}
}

my_key = input('Введите искомый ключ: ')
question = input('Хотите ввести максимальную глубину? Y/N: ').lower()
if question == 'y':
	maximum_depth = int(input('Введите максимальную глубину: '))
	value_key = find_key(site, my_key, maximum_depth)
else:
	value_key = find_key(site, my_key)
print(f'Значение ключа: {value_key}')
