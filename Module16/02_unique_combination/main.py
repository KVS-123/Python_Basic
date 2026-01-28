def merge_sorted_lists(list_1, list_2):
    merged_list = list_1
    merged_list.extend(list_2)
    merged_list.sort()
    last_el = merged_list[-1]
    for i_el in merged_list:
        if i_el == last_el:
            merged_list.remove(i_el)
        last_el = i_el
    return merged_list

list1 = [1, 3, 5, 7, 9]
list2 = [2, 4, 5, 6, 8, 10]
merged = merge_sorted_lists(list1, list2)
print(merged)
