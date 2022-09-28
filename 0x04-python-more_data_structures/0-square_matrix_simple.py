#!/usr/bin/python3
def square_matrix_simple(matrix=[]):
    new_matr = []
    for iterable in matrix:
        new_matr.append(map(square,iterable))
    return new_matr


def square(n):
    return n*n
