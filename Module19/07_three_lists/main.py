def task_1(array1, array2, array3, method):
    if method == 1:
        answer_1 = list()
        for i_elem in array1:
            if i_elem in array2 and i_elem in array3:
                answer_1.append(i_elem)
        print('Решение без множеств:', answer_1)
    elif method == 2:
        set1, set2, set3 = set(array1), set(array2), set(array3)
        answer_2 = set1 & set2 & set3
        print('Решение с множествами:', answer_2)
    else:
        print('неверный способ.')

def task_2(array1, array2, array3, method):
    if method == 1:
        answer_1 = list()
        for i_elem in array1:
            if i_elem not in array2 and i_elem not in array3:
                answer_1.append(i_elem)
        print('Решение без множеств:', answer_1)
    elif method == 2:
        set1, set2, set3 = set(array1), set(array2), set(array3)
        answer_2 = set1 - set2 - set3
        print('Решение с множествами:', answer_2)
    else:
        print('неверный способ.')

array_1 = [1, 5, 10, 20, 40, 80, 100]
array_2 = [6, 7, 20, 80, 100]
array_3 = [3, 4, 15, 20, 30, 70, 80, 120]

print('Задача 1:')
task_1(array_1, array_2, array_3, 1)
task_1(array_1, array_2, array_3, 2)

print('Задача 2:')
task_2(array_1, array_2, array_3, 1)
task_2(array_1, array_2, array_3, 2)
