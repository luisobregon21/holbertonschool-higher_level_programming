#!/usr/bin/python3
''' Module '''


def pascal_triangle(n):
    '''that returns a list of lists of integers representing
       the Pascal’s triangle of n '''

    pascal_list = []
    ''' a container to collect the rows '''
    for _ in range(n):
        row = [1]
        ''' a starter 1 in the row '''
        if pascal_list:
            ''' then we're in the second row or beyond '''
            last_row = pascal_list[-1]
            ''' reference the previous row '''
            ''' stops at the shortest iterable, so for the second row, we have
            nothing in this list comprension, but the third row sums 1 and 1
             and the fourth row sums in pairs. It's a sliding window. '''
            row.extend([sum(pair) for pair in zip(last_row, last_row[1:])])
            ''' finally append the final 1 to the outside '''
            row.append(1)
        pascal_list.append(row)
        ''' add the row to the results. '''
    return pascal_list
