#!/usr/bin/python3
def print_matrix_integer(matrix=[[]]):
    for row in range(len(matrix)):
        for col in range(len(matrix[index])):
            if col != 9:
                print(" ", end='')
            print("{:d}".format(matrix[row][col]), end='')
        print()
