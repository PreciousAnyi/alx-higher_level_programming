#!/usr/bin/python3

def square_matrix_simple(matrix=[]):
    square_element = lambda x: x ** 2
    square_row = lambda row: list(map(square_element,row))
    square_matrix = list(map(square_row, matrix))
    return square_matrix
