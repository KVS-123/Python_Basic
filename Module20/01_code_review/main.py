students = {
    1: {
        'name': 'Bob',
        'surname': 'Vazovski',
        'age': 23,
        'interests': ['biology, swimming']
    },
    2: {
        'name': 'Rob',
        'surname': 'Stepanov',
        'age': 24,
        'interests': ['math', 'computer games', 'running']
    },
    3: {
        'name': 'Alexander',
        'surname': 'Krug',
        'age': 22,
        'interests': ['languages', 'health food']
    }
}


def f(dict_f):
    lst = list()
    string = str()
    for i in dict_f:
        lst.extend(dict_f[i]['interests'])
        string += dict_f[i]['surname']
    return lst, len(string)


pairs = [(people, students[people]['age']) for people in students]
print('Список пар "ID студента — возраст":', pairs)

my_lst, length = f(students)
print('Полный список интересов всех студентов:', my_lst)
print('Общая длина всех фамилий студентов:', length)
