#!/usr/bin/python3
def search_replace(my_list, search, replace):
    if not my_list:
        return my_list
    new_list = []
    for element in my_list:
        if element == search:
            elment = replace
        new_list.append(element)
    return new_list
