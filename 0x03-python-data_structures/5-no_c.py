#!/usr/bin/python3
def no_c(my_string):
    new_string = []
    for char in my_string:
        if char in "Cc":
            continue
        new_string.append(char)
    new_string = "".join(new_string)
    return new_string
