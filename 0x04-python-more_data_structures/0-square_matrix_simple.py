#!/usr/bin/python3
def square_matrix_simple(matrix=[]):
    squ_mat = []
    for l in matrix:
        squ_mat.append([c**2 for c in l])
    return squ_mat
