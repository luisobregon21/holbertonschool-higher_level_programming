#!/usr/bin/python3
def print_matrix_integer(matrix=[[]]):
    if matrix is not None:
        for idx in range(len(matrix)):
            for idx2 in range(len(matrix[idx])):
                print("{:d}".format(matrix[idx][idx2]), end="")
                if idx2 < len(matrix[idx]) - 1:
                    print(" ", end="")
            print()
