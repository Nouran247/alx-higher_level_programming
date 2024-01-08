#!/usr/bin/python3
def print_matrix_integer(matrix=[[]]):
    if not matrix:
        return None
    for i in matrix:
        if len(matrix) == 0:
            print()
        for j in range(len(matrix)):
            print("{:d}".format(i[j]),
                  end = "\n" if (j is len(matrix) - 1)
                  else " ")
