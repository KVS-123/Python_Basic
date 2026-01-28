def quick_sort(lst):
    if len(lst) == 0:
        return []
    else:
        ref_el = lst[-1]
    list_lower = [i for i in lst if i < ref_el]
    list_ref = [i for i in lst if i == ref_el]
    list_bigger = [i for i in lst if i > ref_el]
    sorted_list = quick_sort(list_lower) + list_ref + quick_sort(list_bigger)
    return sorted_list


print(quick_sort([5, 8, 9, 4, 2, 9, 1, 8]))