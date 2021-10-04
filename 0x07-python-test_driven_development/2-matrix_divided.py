#!/usr/bin/python3
''' Module contains a matrix_divide function '''


def matrix_divided(matrix, div):
    ''' function divides all elements of a list
    param:
        matrix: list of lists of integers or floats
        div: number that the elements are being
        divided by.
    '''
    error = "matrix must be a matrix (list of lists) of integers/floats"
    if type(matrix) is not list:
        raise TypeError(error)

    for row in matrix:
        if type(row) is not list:
            raise TypeError(error)
        for element in row:
            if type(element) not in [int, float]:
                raise TypeError(error)

    row_zero_len = len(matrix[0])
    for row in matrix:
        if row_zero_len != len(row):
            raise TypeError("Each row of the matrix must have the same size")

    if type(div) not in [int, float]:
        raise TypeError("div must be a number")

    if div == 0:
        raise ZeroDivisionError("division by zero")

    return [[round(ele / div, 2) for ele in row] for row in matrix]
