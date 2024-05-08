#!/usr/bin/python3
"""Pascal is calling"""


def pascal_triangle(n):
    """Here is a function that do stuff"""
    if n <= 0:
        return []
    if n == 1:
        return [1]
    if n == 2:
        return [[1], [1, 1]]
    my_list_of_lists = [[1], [1, 1]]
    for i in range(2, n + 1, 1):
        my_list_of_lists.append([1] * i)
        for j in range(1, len(my_list_of_lists[i]) - 1, 1):
            my_list_of_lists[i][j] = my_list_of_lists[i - 1][j - 1] + my_list_of_lists[i - 1][j]

    return my_list_of_lists
