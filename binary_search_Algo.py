def binary_search(list_in, item) -> int:
    """
    If item exists in list_in, this function returns its position in the list.
    """
    assert type(item) == int
    assert all([type(x) == int for x in list_in])

    binary_list = sorted(list_in)

    list_start = 0
    list_end = len(list_in) - 1


    while list_start <= list_end:
        mid_pt = list_start + (list_end - list_start) // 2
        midpoint_value = list_in[mid_pt]
        if binary_list[mid_pt] == item:
            return binary_list.index(item)

        elif item < midpoint_value:
            list_end = mid_pt - 1

        else:
            list_start = mid_pt + 1
    return None

list_in_a = [2, 3, 4, 6, 14, 9, 7, 12, 15, 16]

item_a = 15

print(binary_search(list_in_a, item_a))