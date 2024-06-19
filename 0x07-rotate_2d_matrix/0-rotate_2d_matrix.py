#!/usr/bin/python3
"""Rotation in here"""


def rotate_2d_matrix(matrix):
    """
        1 2 3
        4 5 6
        7 8 9

        1 4 7
        2 5 8
        3 6 9

        i j
        [0][0] == [0][0]
        [0][1] == [1][0]
        [0][2] == [2][0]
        [1][1] == [1][1]
        [1][2] == [2][1]
        [2][2] == [2][2]
    """
    for i in range(len(matrix)):
        for j in range(i, len(matrix)):
            temp = matrix[i][j]
            matrix[i][j] = matrix[j][i]
            matrix[j][i] = temp

    for i in range(len(matrix)):
        for j in range(len(matrix[i]) - 1):
            if j < len(matrix[i]) / 2:
                temp = matrix[i][j]
                matrix[i][j] = matrix[i][len(matrix[i]) - 1 - j]
                matrix[i][len(matrix[i]) - 1 - j] = temp
