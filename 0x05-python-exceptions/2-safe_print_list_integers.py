#!/usr/bin/python3
def safe_print_integers(my_list=[], x=0):
    counter = 0
    for i in range(x):
        try:
            print("{:d}".format(my_list[i]), end="")
            i += 1
        except (ValueError, TypeError):
            continue
        print()
        return (counter)
