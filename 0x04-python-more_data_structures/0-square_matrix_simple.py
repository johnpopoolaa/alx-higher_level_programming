#!/usr/bin/bash
def square_matrix_simple(matrix=[]):
    if not matrix:
        return None
    new_list = []
    for row in matrix:
        inner_list = [x * x for x in row]
        new_list.append(inner_list)
    return new_list
