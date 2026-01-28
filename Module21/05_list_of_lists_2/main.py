def rec_fun(lst):
    new_list = list()
    for i in lst:
        if isinstance(i, list):
            new_list.extend(rec_fun(i))
        else:
            new_list.append(i)
    return new_list


nice_list = [1, 2, [3, 4], [[5, 6, 7], [8, 9, 10]],
             [[11, 12, 13], [14, 15], [16, 17, 18]]]

print(rec_fun(nice_list))