#!/usr/bin/python3
def safe_print_integers(my_list=[], x=0):
    if not my_list:
        return 0
    i = 0
    for i in range(x):
        try:
            print("{:d}".format(my_list[i]), end='')
            i += 1
        except (ValueError, TypeError):
            continue
        print()
        return i
