#!/usr/bin/python3
def print_reversed_list_integer(my_list=[]):
    i = -1
    while i >= -1 * len(my_list):
        print('{:d}'.format(my_list[i]))
        i -= 1
