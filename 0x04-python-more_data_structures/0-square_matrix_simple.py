#!/usr/bin/python3

def square_matrix_simple(matrix=[]):
    square_matrix = []
    for elem in matrix:
        result = list(map(lambda x: x ** 2, elem))
        square_matrix.append(result)
    return square_matrix
