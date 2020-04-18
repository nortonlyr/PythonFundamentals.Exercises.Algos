def binary_search(list_in, item) -> int:
    """
    If item exists in list_in, this function returns its position in the list.
    """
    list_start = 0
    list_end = len(list_in) - 1

    while list_start <= list_end:
        midpoint = list_start + (list_end - list_start) // 2
        midpoint_value = list_in[midpoint]
        if midpoint_value == item:
            return midpoint

        elif item < midpoint_value:
            list_end = midpoint - 1

        else:
            list_start = midpoint + 1
    return None

list_in_a = [2, 3, 4, 6, 7, 9, 12, 14, 15, 16]

item_a = 9

print(binary_search(list_in_a, item_a))