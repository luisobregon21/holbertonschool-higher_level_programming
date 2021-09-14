#!/usr/bin/python3
def max_integer(my_list=[]):
    if len(my_list) == 0:
        return None
    big_num = my_list[0]
    for num in my_list:
        if num > big_num:
            big_num = num
    return big_num
