#!/usr/bin/python3
def weight_average(my_list=[]):
    if not my_list:
        return 0
    new_list = list(map(lambda x: x[0] * x[1], my_list))
    weight = list(map(lambda x: x[1], my_list))
    return sum(new_list) / sum(weight)
