#!/usr/bin/python3

'''
Module that rotates a 2D matrix in a 90 degrees
'''


def rotate_2d_matrix(matrix):
    '''
    Rotate a 2d matrix
    '''
    n = len(matrix)

    for i in range(n):
        for j in range(i + 1, n):
            matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]
    for row in matrix:
        row.reverse()

    return matrix
