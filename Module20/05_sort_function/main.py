def tpl_sort(tpl):
    new_list = list(tpl)
    for i in new_list:
        if i % 1 != 0:
            return tpl
    new_list.sort()
    return tuple(new_list)

tuple_test = (6, 3, -1, 8, 4, 10, -5)
print(tpl_sort(tuple_test))