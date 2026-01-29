import os


def find_file(start_dir_path):
    for path, direct, file in os.walk(start_dir_path):
        print(f'\nПоиск файлов в директории: \n{path}')
        for i_file in file:
            if i_file[-3::] == '.py':
                print(f'файл: {i_file}')
                yield count_str(os.path.join(path, i_file))


def count_str(file):
    count = 0
    with open(file, 'r', encoding='UTF-8') as r_file:
        for line in r_file:
            if line[0] != '#' and len(line.split()) != 0:
                count += 1
    return count


abs_path = os.path.abspath(os.path.join('..', '..'))
for elem in find_file(abs_path):
    print(elem)
