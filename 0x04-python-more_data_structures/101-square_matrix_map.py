#!/usr/bin/python3
def complex_delete(my_dict, value):
    tmp = my_dict.copy()
    for i, val in tmp.items():
        if value == val:
            my_dict.pop(i)
    return my_dict
